from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import PDBWriter

# Create Molecule from SMILES
smiles = "CC(=O)NC1=CC=C(C=C1)O"
molecule = Chem.MolFromSmiles(smiles)

# Add Explicit hydrogen atoms
molecule = Chem.AddHs(molecule)

# Generate 3D Coordinates
AllChem.EmbedMolecule(molecule)

# Save the molecule in PDB Format
output_file = "output_Hyd.pdb"
with PDBWriter(output_file) as writer:
    writer.write(molecule)