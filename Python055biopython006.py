from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs

# Create a molecule from a SMILES string
smiles = "CCO"
mol = Chem.MolFromSmiles(smiles)

# Generate the Morgan fingerprint for the molecule
fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2)

# Convert the fingerprint to a list of integers
fp_list = DataStructs.BitVectToText(fp)
print(f"Fingerprint as list of integers: {fp_list}")