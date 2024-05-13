#!/bin/bash
#Once BPE models trained, apply to corpora, add "\b" with bpe_mr segmented text data to the original corpora

mkdir ./seg_data
mkdir ./seg_data/raw
mkdir ./seg_data/data

for lang in arp git lez ntu nyb ddo usp
do
    echo "Now processing $lang"
    #Apply BPE model to train corp
    subword-nmt apply-bpe -c bpemr_models/$lang.*.model<./tokenizer_in_corp/${lang}_train.txt>./seg_data/raw/raw_bpe_train.$lang.txt
    #Create manual merged version of train corpus
    python3 manual_merges.py --in_file ./seg_data/raw/raw_bpe_train.$lang.txt --out_file ./seg_data/raw/merged_bpe_train.$lang.txt
    #Apply BPE model to val corp
    subword-nmt apply-bpe -c bpemr_models/$lang.*.model<./tokenizer_in_corp/${lang}_val.txt>./seg_data/raw/raw_bpe_val.$lang.txt
    #Create manual merged version of val corpus
    python3 manual_merges.py --in_file ./seg_data/raw/raw_bpe_val.$lang.txt --out_file ./seg_data/raw/merged_bpe_val.$lang.txt
    #Apply BPE model to test corp
    subword-nmt apply-bpe -c bpemr_models/$lang.*.model<./tokenizer_in_corp/${lang}_test.txt>./seg_data/raw/raw_bpe_test.$lang.txt
    #Create manual merged version of test corpus
    python3 manual_merges.py --in_file ./seg_data/raw/raw_bpe_test.$lang.txt --out_file ./seg_data/raw/merged_bpe_test.$lang.txt
    #add \b annotation to train_uncovered track1, val uncovered track1 (dev data), and val covered track1 (test data)
    python3 add_b_line.py --language $lang
done