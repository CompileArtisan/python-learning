from rdkit import Chem
import pandas as pd

# Define the smiles string and convert it into a molecule object
smiles = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"
mol = Chem.MolFromSmiles(smiles)

# Create a DataFrame with atom information in a single line
df = pd.DataFrame({
    "Atom_index": [atom.GetIdx() for atom in mol.GetAtoms()],
    "Atomic Number": [atom.GetAtomicNum() for atom in mol.GetAtoms()],
    "Is Aromatic": [atom.GetIsAromatic() for atom in mol.GetAtoms()],
    "Atom_symbol": [atom.GetSymbol() for atom in mol.GetAtoms()],
})

# Save the DataFrame to an Excel file
df.to_excel("atom_info.xlsx", index=False)
print(df)