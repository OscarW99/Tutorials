import requests
import xml.etree.ElementTree as ET

# Set the UniProt ID for the protein you want to retrieve information about
uniprot_id = "P69905"

# Set the URL for the UniProt API
url = f"https://www.uniprot.org/uniprot/{uniprot_id}.xml"
print(f"URL: {url}")

# Send a request to the API and retrieve the response
response = requests.get(url)

# Parse the XML response
root = ET.fromstring(response.content)

# Extract the UniProt ID, protein name, and protein sequence
entry = root.find("{http://uniprot.org/uniprot}entry")
accession = entry.find("{http://uniprot.org/uniprot}accession").text
protein_name = entry.find("{http://uniprot.org/uniprot}protein/{http://uniprot.org/uniprot}recommendedName/{http://uniprot.org/uniprot}fullName").text
sequence = entry.find("{http://uniprot.org/uniprot}sequence").text

# Print the UniProt ID, protein name, and protein sequence
print(f"UniProt ID: {accession}")
print(f"Protein name: {protein_name}")
print(f"Protein sequence: {sequence}")




# UniProt is a database of protein sequences and related information.
# every protein that is included in the UniProt database has a unique UniProt ID. This ID is a combination of letters 

# The UniProt database contains information about the amino acid sequences, structures, functions, interactions, and post-translational modifications of proteins from a wide range of organisms.

#The UniProt API is a REST API.

# In addition to protein sequences, UniProt also provides annotation data that describes various aspects of protein function and structure, such as domains, motifs, and active sites.