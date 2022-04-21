#!/bin/bash

## init
# python -m batch_feature_extraction 12

# 1
#python -m train_seldnet 12 1

## 2
python -m batch_feature_extraction 3
python -m train_seldnet 3 2
