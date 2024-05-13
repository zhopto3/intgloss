#!/bin/bash

declare -i init=1     #initial merge
declare -i final=350   #final merge
declare -i step=1     #Step size

mkdir ./bpemr_models
mkdir ./temp_storage

for lang in arp git lez ntu nyb ddo usp
do
    echo "Now processing $lang"
    #Create input corpus
    python3 tokenizer_input.py --language $lang
    #Make full train corpus
    cat ./tokenizer_in_corp/${lang}_train.txt ./tokenizer_in_corp/${lang}_val.txt>./tokenizer_in_corp/${lang}_full.txt
    for ((i=init; i<=final; i=i+step))
    do
        #Train bpe model with i merges
        subword-nmt learn-bpe -s $i<./tokenizer_in_corp/${lang}_full.txt>temp_storage/$lang.$i.model
        #Apply bpe model (monolingually)
        subword-nmt apply-bpe -c temp_storage/$lang.$i.model<./tokenizer_in_corp/${lang}_full.txt>temp_storage/$lang.$i.txt
        #Calculate subword frequencies over the BPE segmented corpus
        python3 ./freq.py temp_storage/$lang.$i.txt
        #Test stop condition for BPE
        val=$(python3 ./early_stop.py --merge $i --model_file "temp_storage/$lang.$i.model" --freq_file temp_storage/$lang.$i.txt.freqs.tsv)
        if [ "$val" == "True" ]
        then
            #Move final corpus & model out of temp_storage
            mv temp_storage/$lang.$i.model ./bpemr_models
            echo "Stopping at merge $i"
            break
        fi  
    done
    #in case there's no early stopping, use 300
    if [ $i == 351 ]
    then
        i=300
        mv temp_storage/$lang.$i.model ./bpemr_models
    fi
done

#Delete the rest of the files
rm -r ./temp_storage