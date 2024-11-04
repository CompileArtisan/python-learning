# Frequency of motifs using bio python
from Bio.Seq import Seq

# Defind the sequence and the motif to search for
sequence = Seq("ACGACGACGACGACG")
motif = Seq("ACG")

# Calculate the length of the sequence
sequence_length = len(sequence)

# Calculate the frequency of motif in the sequence
motif_count = sequence.count(motif)
motif_frequency = motif_count / len(sequence)

# Print sequence length and motif frequency
print(f"Sequence length: {len(sequence)}")
print(f"Motif count: {motif_count}")
print(f"Motif frequency: {motif_frequency}")