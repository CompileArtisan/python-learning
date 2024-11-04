# finding motif in  multilined sequences

from Bio.Seq import Seq
from Bio import SeqUtils, SeqIO

# Define the pattern and sequence
pattern = Seq("GC")

# Find the sequence from the file "pancreatic_cancer_sequences.txt"
with open("pancreatic_cancer_sequences.txt", "r") as file:
    for seq in SeqIO.parse(file, "fasta"):
        # Perform the search
        result = SeqUtils.nt_search(str(seq.seq), str(pattern))

        # Get positions (excluding the first element, which is the pattern itself)
        positions = result[1:]

        # Collect the positions with start and end indices
        results_with_indices = [(pos, pos + len(pattern)) for pos in positions]
        print(f"Pattern found at positions: {results_with_indices}")
