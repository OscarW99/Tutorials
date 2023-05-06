
# On terminal...
# pip install glassdoor

# import requests

# response = requests.get(
#     "http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=120&t.k=fz6JLNDfgVs&action=employers&q=pharmaceuticals&userip=192.168.43.42&useragent=Mozilla/%2F4.0")

import os
from linkedin_api import Linkedin
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / 'Glassdoor\\.env'
load_dotenv(dotenv_path=env_path)

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

api = Linkedin(EMAIL, PASSWORD)

job_search = api.search_jobs()

# * get_job(job_id)
# Fetch data about a given job. :param job_id: LinkedIn job ID :type job_id: str

# Returns:	Job data
# Return type:	dict
# ----------------------------------

# * search(params, limit=-1, offset=0)
# Perform a LinkedIn search.

# Parameters:
# params (dict) – Search parameters (see code)
# limit (int, optional) – Maximum length of the returned list, defaults to -1 (no limit)
# offset (int, optional) – Index to start searching from
# Returns:
# List of search results

# Return type:
# list
# ----------------------------------

# * search_jobs(keywords=None, companies=None, experience=None, job_type=None, job_title=None, industries=None,
#             location_name=None, remote=False, listed_at=86400, distance=None, limit=-1, offset=0, **kwargs)
# Perform a LinkedIn search for jobs.

# Parameters:
# keywords(str, optional) – Search keywords(str)
# companies(list, optional) – A list of company URN IDs(str)
# experience(list, optional) – A list of experience levels, one or many of “1”, “2”, “3”, “4”, “5” and “6” (internship, entry level, associate, mid-senior level, director and executive, respectively)
# job_type(list, optional) – A list of job types, one or many of “F”, “C”, “P”, “T”, “I”, “V”, “O” (full-time, contract, part-time, temporary, internship, volunteer and “other”, respectively)
# job_title(list, optional) – A list of title URN IDs(str)
# industries(list, optional) – A list of industry URN IDs(str)
# location_name(str, optional) – Name of the location to search within. Example: “Kyiv City, Ukraine”
# remote(boolean, optional) – Whether to search only for remote jobs. Defaults to False.
# listed_at(int/str, optional. Default value is equal to 24 hours.) – maximum number of seconds passed since job posting. 86400 will filter job postings posted in last 24 hours.
# distance(int/str, optional. If not specified, None or 0, the default value of 25 miles applied.) – maximum distance from location in miles
# limit(int, optional, default - 1) – maximum number of results obtained from API queries. -1 means maximum which is defined by constants and is equal to 1000 now.
# offset(int, optional) – indicates how many search results shall be skipped
# Returns:
# List of jobs

# Return type:
# list
