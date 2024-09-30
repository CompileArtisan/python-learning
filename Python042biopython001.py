from Bio import Entrez

# Set the email address for NCBI
Entrez.email = "vasavi.cs@gmail.com"

# Search for nucleotide sequences related to "pancreatic cancer" in Homo sapiens
search_results = Entrez.read(Entrez.esearch(db='nucleotide', retmax=10, term="pancreatic cancer[Title] AND Homo Sapiens[Organism]"))

# Get the list of IDs
IDs = search_results["IdList"]
print("Retrieved IDs:", IDs)

# Open the file to save the sequences
with open("pancreatic_cancer_sequences.txt", "w") as output_file:
    # Loop through each ID to fetch the sequence
    for ID in IDs:
        try:
            # Fetch the sequence in FASTA format
            sequence = Entrez.efetch(db="nucleotide", id=ID, rettype="fasta", retmode='text').read()
            output_file.write(sequence + "\n")
        except Exception as e:
            print(f"An error occurred with ID {ID}: {e}")

print("Sequence retrieval and file writing complete.")