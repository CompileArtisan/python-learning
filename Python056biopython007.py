import re
seq = "ATGCGATCGACHCTAG"
motif = "CGA"
pattern = re.compile(motif)
matches = pattern.finditer(seq)
for match in matches:
    print(match.start(), match.end())