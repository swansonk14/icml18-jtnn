from rdkit import Chem
from optparse import OptionParser
from tqdm import tqdm

MAX_RING_SIZE = 8

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-d", "--data_path", dest="data_path")
    parser.add_option("-s", "--save_path", dest="save_path")
    args, _ = parser.parse_args()

    num_lines = 0
    with open(args.data_path, 'r') as rf:
        rf.readline()
        for line in rf:
            num_lines += 1

    with open(args.data_path, 'r') as rf, open(args.save_path, 'w') as wf:
        header = rf.readline()
        wf.write(header.strip() + '\n')
        for line in tqdm(rf, total=num_lines):
            smiles = line.strip().split(',')[0]
            mol = Chem.MolFromSmiles(smiles)
            should_write = True
            for atom in mol.GetAtoms():
                if atom.IsInRing():
                    if all([not atom.IsInRingSize(i) for i in range(1, MAX_RING_SIZE+1)]):
                        should_write = False
                        break
            if should_write:
                wf.write(line.strip() + '\n')

