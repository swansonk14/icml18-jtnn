import sys
sys.path.append('..')

import rdkit
import rdkit.Chem as Chem
import copy
from fast_jtnn import *

if __name__ == "__main__":
    from argparse import ArgumentParser
    from tqdm import tqdm

    lg = rdkit.RDLogger.logger()
    lg.setLevel(rdkit.RDLogger.CRITICAL)

    parser = ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True)
    parser.add_argument('--save_path', type=str, required=True)
    args = parser.parse_args()

    with open(args.data_path) as f:
        lines = f.readlines()

    cset = set()
    for line in tqdm(lines, total=len(lines)):
        smiles = line.split()[0]
        mol = MolTree(smiles)
        for c in mol.nodes:
            cset.add(c.smiles)

    with open(args.save_path, 'w') as f:
        for x in cset:
            f.write(x + '\n')