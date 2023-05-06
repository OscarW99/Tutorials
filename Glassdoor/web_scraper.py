import asyncio
import json
import math
import os
import re
from collections import defaultdict
from typing import Dict, List, Optional
from pathlib import Path

# TODO: Set for different countries and job titles.

from scrapfly import ScrapeApiResponse, ScrapeConfig, ScrapflyClient

client = ScrapflyClient(key=os.environ["SCRAPFLY_KEY"], max_concurrency=10)
BASE_CONFIG = {
    # we want can select any country proxy:
    "country": "US",
    "asp": True,
    # To see Glassdoor results of a specific country we must set a cookie:
    "cookies": {"tldp": "1"}
}


def find_json_objects(text: str, decoder=json.JSONDecoder()):
    """Find JSON objects in text, and generate decoded JSON data and it's ID"""
    pos = 0
    while True:
        match = text.find("{", pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            # backtrack to find the key/identifier for this json object:
            key_end = text.rfind('"', 0, match)
            key_start = text.rfind('"', 0, key_end)
            key = text[key_start + 1 : key_end]
            yield key, result
            pos = match + index
        except ValueError:
            pos = match + 1


def extract_apollo_state(result: ScrapeApiResponse) -> Dict:
    """Extract apollo graphql state data from HTML source"""
    data = re.findall('apolloState":\s*({.+})};', result.content)[0]
    return json.loads(data)


def extract_apollo_cache(result: ScrapeApiResponse) -> Dict[str, List]:
    """Extract apollo graphql cache data from HTML source"""
    script_with_cache = result.selector.xpath("//script[contains(.,'window.appCache')]/text()").get()
    cache = defaultdict(list)
    for key, data in find_json_objects(script_with_cache):
        cache[key].append(data)
    return cache


def parse_salaries(result: ScrapeApiResponse) -> Dict:
    """parse jobs page for salary data"""
    cache = extract_apollo_state(result)
    xhr_cache = cache["ROOT_QUERY"]
    salaries = next(v for k, v in xhr_cache.items() if k.startswith("salariesByEmployer") and v.get("results"))
    return salaries


async def scrape_salaries(employer: str, employer_id: str, max_pages: Optional[int] = None) -> Dict:
    """Scrape salary listings"""
    # scrape first page of jobs:
    first_page_url = f"https://www.glassdoor.com/Salaries/{employer}-Salaries-E{employer_id}.htm?filter.countryId={BASE_CONFIG['cookies']['tldp']}&minRating=0.0"
    first_page = await client.async_scrape(ScrapeConfig(url=first_page_url, **BASE_CONFIG))
    salaries = parse_salaries(first_page)
    total_pages = salaries["pages"]
    if max_pages and total_pages > max_pages:
        total_pages = max_pages

    print(f"scraped first page of salaries, scraping remaining {total_pages - 1} pages")
    other_pages = [
        ScrapeConfig(url=f"{first_page_url}&pageNumber={page}", **BASE_CONFIG)
        for page in range(2, total_pages + 1)
    ]
    async for result in client.concurrent_scrape(other_pages):
        salaries["results"].extend(parse_salaries(result)["results"])
    return salaries

async def find_companies(query: str):
    """find company Glassdoor ID and name by query. e.g. "ebay" will return "eBay" with ID 7853"""
    result = await client.async_scrape(
        ScrapeConfig(
            url=f"https://www.glassdoor.com/searchsuggest/typeahead?numSuggestions=8&source=GD_V2&version=NEW&rf=full&fallback=token&input={query}",
            **BASE_CONFIG,
        )
    )
    data = json.loads(result.content)
    return data[0]["suggestion"], data[0]["employerId"]


async def scrape_salaries(employer: str, employer_id: str, location: str) -> Dict:
    """Scrape salary listings for bioinformatics jobs"""
    # scrape first page of salaries:
    first_page_url = f"https://www.glassdoor.com/Salaries/{employer}-Salaries-E{employer_id}.htm?clickSource=searchBtn&jobTitle={location}%20bioinformatics&location={location}"
    first_page = await client.async_scrape(ScrapeConfig(url=first_page_url, **BASE_CONFIG))
    salaries = parse_salaries(first_page)
    total_pages = salaries["pages"]

    print(f"scraped first page of salaries, scraping remaining {total_pages - 1} pages")
    other_pages = [
        ScrapeConfig(url=f"{first_page_url}&page={page}", **BASE_CONFIG)
        for page in range(2, total_pages + 1)
    ]
    async for result in client.concurrent_scrape(other_pages):
        salaries["results"].extend(parse_salaries(result)["results"])
    return salaries


async def run():
    """Scrape salary information for bioinformatics jobs and save results to a JSON file"""
    out_dir = Path(__file__).parent / "results"
    out_dir.mkdir(exist_ok=True)

    # find the employer ID for Glassdoor
    emp_name, emp_id = await find_companies("bioinformatics")
    print(f"Scraping salary information for {emp_name} (ID: {emp_id})")

    # scrape salaries for bioinformatics jobs in various locations
    locations = ["United States", "Canada", "United Kingdom"]
    for location in locations:
        salaries = await scrape_salaries(emp_name, emp_id, location)
        out_file = out_dir.joinpath(f"{location.lower().replace(' ', '_')}_salaries.json")
        out_file.write_text(json.dumps(salaries, indent=2))
        print(f"Saved salary data for {location} to {out_file}")

if __name__ == "__main__":
    asyncio.run(run())

