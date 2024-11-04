# finding motif in single-lined sequences

from Bio.Seq import Seq
from Bio import SeqUtils

# Define the pattern and sequence
pattern = Seq("ACG")
sequence = Seq("ACGACGACGACGACG")

# Perform the search
result = SeqUtils.nt_search(str(sequence), str(pattern))

# Get positions (excluding the first element, which is the pattern itself)
positions = result[1:]

# Collect the positions with start and end indices
results_with_indices = [(pos, pos + len(pattern)) for pos in positions]
print(f"Pattern found at positions: {results_with_indices}")