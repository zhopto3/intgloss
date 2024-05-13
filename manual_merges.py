"""Script that identifies BPE merges and keeps track of them, then merges the rest of 
the units manually.
Author: Zachary W. Hopton
"""
from collections import Counter
import re
import argparse


def get_args():
    parser = argparse.ArgumentParser("Script to manually merge adjacent single characters")

    parser.add_argument("--in_file", required=True,
                        help="Path to input file that has been BPE tokenized")
    parser.add_argument("--out_file", required=True,
                        help="Path to output file; BPE segmented and merged single adjacent characters")
    
    return parser.parse_args()


def get_words(units:list)->list:
    grouped = []
    word = []
    for unit in units:
        if "@@" in unit:
            word.append(unit)
        else:
            word.append(unit)
            grouped.append(word)
            word = []

    return grouped


def process_line(line:str)->tuple:
    words = get_words(line.split())
    out=[]

    for word in words:
    #Check if the word contains any BPE merges
        if len(word)==1 and len(word[0])==1:
            #Single character words should be counted as bpe merges
            #BPE_merges.append(word[0])
            out.append(word[0])
        else:
            current_word =""
            current_manual = ""
            for units in word:
                # >= 2 because we only want merged units (not single characters, unless they're words)
                #if len(units.rstrip('@'))>=2:
                if len(re.sub(r"@@$","",units))>=2:
                    if len(current_manual)!=0:
                        #current_word+=current_manual+"-"
                        current_word+=current_manual+"@@ "
                        #current_word+=re.sub(r"@@$","",units)+"-"
                        current_word+=units + " "
                        current_manual=""
                    else:
                        #current_word+=re.sub(r"@@$","",units)+"-"
                        current_word+=units + " "
                else:
                    current_manual+=re.sub(r"@@$","",units)
            if len(current_manual)!= 0:
                #No dash because this will be at the end of the word
                current_word+=current_manual
            #Add word to output line, without any leftover dashes from bpe merges
            #out.append(current_word.rstrip("-"))
            out.append(current_word)

    return " ".join(out)
    # while re.search(r" (.)@@ (.)@@ ", line) or re.search(r" (.)@@ (.)(\s)", line) or re.search(r"^(.)@@ (.)@@",line) or re.search(r"^(.)@@ (.)(\s)",line):
    #     line = re.sub(r"^(.)@@ (.)(\s)",r"\1\2\3", line)
    #     line = re.sub(r"^(.)@@ (.)@@",r"\1\2@@ ", line)
    #     line = re.sub(r" (.)@@ (.)@@ ",r" \1\2@@ ",line)
    #     line = re.sub(r" (.)@@ (.)(\s)",r" \1\2\3",line)

    # return line


def main(in_file, out_file):
    with open(in_file,"r",encoding="utf-8") as inpt, open(out_file, "w",encoding="utf-8") as otpt:
        for line in inpt:
            #BPE,Manual = process_line(line)
            output = process_line(line)
            #Can append each line to some new file
            output = re.sub(r"(\s){2,}",r"\1",output)
            otpt.write(output+"\n")


if __name__ == "__main__":
    args = get_args()
    main(args.in_file, args.out_file)