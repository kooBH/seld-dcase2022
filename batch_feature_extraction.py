# Extracts the features, labels, and normalizes the development and evaluation split features.

import cls_feature_class
import parameters
import sys

import argparse

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, required=True,help='user parameter set defined by user')
    parser.add_argument('--mix','-m', type=bool, default=False,help='using synth data')
    args = parser.parse_args()
    # Expects one input - task-id - corresponding to the configuration given in the parameter.py file.
    # Extracts features and labels relevant for the task-id
    # It is enough to compute the feature and labels once. 


    task_id = args.id
    params = parameters.get_params(task_id)

    # -------------- Extract features and labels for development set -----------------------------
    dev_feat_cls = cls_feature_class.FeatureClass(params,synth=args.mix)

    # # Extract features and normalize them
    dev_feat_cls.extract_all_feature()
    dev_feat_cls.preprocess_features()

    # # Extract labels
    dev_feat_cls.extract_all_labels()

if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except (ValueError, IOError) as e:
        sys.exit(e)

