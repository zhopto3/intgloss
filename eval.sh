#!/bin/bash
mkdir ./pred_retrained_char/eval

for lang in Gitksan Arapaho Lezgi Natugu Nyangbo Tsez Uspanteko
do
    #Evaluate without manual merging
    python3 baseline/src/eval.py --pred pred_retrained_char/${lang}_track1_morph_trial1.prediction --gold data/$lang/*test-track1-uncovered > ./pred_retrained_char/eval/char_$lang.txt
    #and then with manual merging
    # python3 baseline/src/eval.py --pred bpemr_charhp_pred/${lang}_morph_track1_merged.prediction --gold data/$lang/*test-track1-uncovered > ./bpemr_charhp_pred/eval/merged_$lang.txt

done