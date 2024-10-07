from rdkit import Chem
from rdkit.Chem import Draw, Descriptors
from PIL import Image

# Create molecule from SMILES
# Simplified Molecular Input Line Entry System
smiles = "CC(=O)NC1=CC=C(C=C1)O"
molecule = Chem.MolFromSmiles(smiles)

# Draw molecule
img = Draw.MolToImage(molecule, size=(400, 200))

# Save the image to a File
img.save("molecule.png")

# Calculate Descriptors for the molecule
descriptors = {
    "Molecular Weight": Descriptors.MolWt(molecule),
    "Number of Heavy Atoms": Descriptors.HeavyAtomCount(molecule),
    "LogP": Descriptors.MolLogP(molecule),
    "H-Bond Donors": Descriptors.NumHDonors(molecule),
    "H-Bond Acceptors": Descriptors.NumHAcceptors(molecule),
}

# Display the image and descriptors
img.show()
print("Descriptors:")
for key, value in descriptors.items():
    print(f"\t{key}: {value}")
