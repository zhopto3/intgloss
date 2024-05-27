#!/bin/bash

for lang in Gitksan Arapaho Lezgi Natugu Nyangbo Tsez Uspanteko
do
    #Get best hyperparam for non manually merged bpe 300 models
    python3 hyperparameter_tuning.py --language $lang --track 1 --datapath "seg_data/data/" --model "morph" --trials 50
    #and then with manual merging
    python3 hyperparameter_tuning.py --language $lang --track 1 --datapath "seg_data/data/" --model "morph" --trials 50 --merged
done