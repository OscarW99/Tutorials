
# pip install biopython

from Bio import Entrez
import json

#  The Bio.Entrez module in Biopython provides a Python wrapper around the NCBI E-utilities API


# Entrez.email = "your_email_address_here"
Entrez.email = ""

# Can return as HTML, json, xml
handle = Entrez.efetch(db="pubmed", id="32817238", rettype="xml", retmode="text")
# Under the hood: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=32817238&rettype=xml&retmode=text

record = Entrez.read(handle) # Returns a python dictionary

print(record)



print(json.dumps(record, indent=4))

title = record["PubmedArticle"][0]["MedlineCitation"]["Article"]["ArticleTitle"]
abstract = record["PubmedArticle"][0]["MedlineCitation"]["Article"]["Abstract"]["AbstractText"]

print("Title:", title)
print("Abstract:", abstract)


