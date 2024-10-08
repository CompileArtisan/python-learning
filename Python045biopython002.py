from Bio import Entrez, SeqIO
Entrez.email = "varunadhitya.balaji@gmail.com"
nucleotide_search = Entrez.read(Entrez.esearch(db="nucleotide", 
                                            retmax=5, 
                                            term="sars[Title] AND Homo Sapiens[Organism]",
                                            sort="PDAT"))
protein_search = Entrez.read(Entrez.esearch(db="protein", 
                                            retmax=5, 
                                            term="sars[Title] AND Homo Sapiens[Organism]",
                                            sort="PDAT"))
gene_search = Entrez.read(Entrez.esearch(db="gene", 
                                            retmax=5, 
                                            term="sars[Title] AND Homo Sapiens[Organism]",
                                            sort="PDAT"))

nucleotide_IDs = nucleotide_search["IdList"]
protein_IDs = protein_search["IdList"]
gene_IDs = gene_search["IdList"]
with open("sars_nucleotide.txt", "w") as file:
    for ID in nucleotide_IDs:
        try:
            sequence = Entrez.efetch(db="nucleotide", id=ID, rettype="fasta", retmode="text").read()
            file.write(sequence + "\n")
        except Exception as e:
            print(f"Error occured with nucleotide ID {ID}: ", e)

with open("sars_gene.txt", "w") as file:
    for ID in gene_IDs:
        try:
            handle = Entrez.efetch(db="gene", id="100423062", retmode="xml")
            record = Entrez.read(handle)
            handle.close()
            id = record[0]['Entrezgene_locus'][0]['Gene-commentary_accession']
            fromS = record[0]['Entrezgene_locus'][0]['Gene-commentary_seqs'][0]['Seq-loc_int']['Seq-interval']['Seq-interval_from']
            toS = record[0]['Entrezgene_locus'][0]['Gene-commentary_seqs'][0]['Seq-loc_int']['Seq-interval']['Seq-interval_to']
            sequence = Entrez.efetch(db="nucleotide", id=id, rettype="fasta", retmode="text", seq_start=fromS, seq_stop=toS).read()
            file.write(sequence + "\n")
        except Exception as e:
            print(f"Error occured with gene ID {ID}: ", e)

with open("sars_protein.txt", "w") as file:
    for ID in protein_IDs:
        try:
            sequence = Entrez.efetch(db="protein", id=ID, rettype="fasta", retmode="text").read()
            file.write(sequence + "\n")
        except Exception as e:
            print(f"Error occured with protein ID {ID}: ", e)
print("Sequence retrival complete")
with open("sars_nucleotide.txt") as file:
    print("NUCLEOTIDES")
    print()
    for seq in SeqIO.parse(file, 'fasta'):
        print(seq.id, ":")
        print("-"*len(seq.id) + "--")
        lengthOfSeq = len(seq.seq)
        print(f"\tNumber of base pairs = {lengthOfSeq//2}")
with open("sars_gene.txt") as file:
    print("NUCLEOTIDES")
    print()
    for seq in SeqIO.parse(file, 'fasta'):
        print(seq.id, ":")
        print("-"*len(seq.id) + "--")
        lengthOfSeq = len(seq.seq)
        print(f"\tNumber of base pairs = {lengthOfSeq//2}")


with open("sars_protein.txt") as file:
    print("NUCLEOTIDES")
    print()
    for seq in SeqIO.parse(file, 'fasta'):
        print(seq.id, ":")
        print("-"*len(seq.id) + "--")
        lengthOfSeq = len(seq.seq)
        print(f"\tNumber of amino acids = {lengthOfSeq}")

# The above code snippet retrieves nucleotide, protein, and gene sequences related to "SARS coronavirus