from optparse import OptionParser
from scipy import sparse
import pickle

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-d", "--smiles_path", dest="smiles_path")
    parser.add_option("-f", "--features_path", dest="features_path")
    parser.add_option("-s", "--save_path", dest="save_path")
    args, _ = parser.parse_args()

    with open(args.smiles_path, 'r') as rf, open(args.features_path, 'rb') as ff, open(args.save_path, 'wb') as wf:
        features_dict = {}
        features = pickle.load(ff)
        rf.readline()
        count = 0
        for line in rf:
            smiles = line.strip().split(',')[0]
            features_dict[smiles] = features[count]
            count += 1
        assert count == features.shape[0] # ensure aligned properly
        pickle.dump(features_dict, wf)