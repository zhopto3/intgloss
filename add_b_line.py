import os
import argparse
import re

def get_args():
    args = argparse.ArgumentParser()
    args.add_argument("--language",choices=["arp","git","lez","ntu","nyb","ddo","usp"],
                      required = True)
    return args.parse_args()


def main():
    args = get_args()

    language_code_mapping = {
        "arp": "Arapaho",
        "git": "Gitksan",
        "lez": "Lezgi",
        "ntu": "Natugu",
        "nyb": "Nyangbo",
        "ddo": "Tsez",
        "usp": "Uspanteko",
    }
    language_code = args.language
    language = language_code_mapping[language_code]
    train_file = f"./data/{language}/{language_code}-train-track1-uncovered"
    validation_file = f"./data/{language}/{language_code}-dev-track1-uncovered"
    test_file = f"./data/{language}/{language_code}-dev-track1-covered"
    true_test = f"./data/{language}/{language_code}-test-track1-covered"
    os.makedirs(f"./seg_data/data/{language}",exist_ok=True)

    #add \b annotation to train data
    with (open(train_file,"r",encoding="utf-8") as train_in,
          open(f"seg_data/data/{language}/{language_code}-train-track1-uncovered","w",encoding="utf-8") as train_out,
          open(f"seg_data/raw/raw_bpe_train.{language_code}.txt","r",encoding="utf-8") as bpe_seg,
          open(f"seg_data/raw/merged_bpe_train.{language_code}.txt","r",encoding="utf-8") as merged_seg):
        #replace inner word w dashes and merge everything as if they were morphemes; add "\b" flag
        b_lines = ["\\b "+re.sub("@@ ","-",line) for line in bpe_seg]
        merged_lines = ["\\q "+re.sub("@@ ","-",line) for line in merged_seg]
        i = 0
        for line in train_in:
            if re.search(r"\\t\s",line):
                train_out.write(line)
                #remove excessive hyphens by reducing to one. 
                current_b = b_lines[i]
                current_bm = merged_lines[i]
                train_out.write(re.sub(r"-+","-",current_b))
                train_out.write(re.sub(r"-+","-",current_bm))
                i+=1
            else:
                train_out.write(line)

    #add \b annotation to val data
    with (open(validation_file,"r",encoding="utf-8") as val_in,
          open(f"seg_data/data/{language}/{language_code}-dev-track1-uncovered","w",encoding="utf-8") as val_out,
          open(f"seg_data/raw/raw_bpe_val.{language_code}.txt","r",encoding="utf-8") as bpe_seg,
          open(f"seg_data/raw/merged_bpe_val.{language_code}.txt","r",encoding="utf-8") as merged_seg):
        #replace inner word w dashes and merge everything as if they were morphemes; add "\b" flag
        b_lines = ["\\b "+re.sub("@@ ","-",line) for line in bpe_seg]
        merged_lines = ["\\q "+re.sub("@@ ","-",line) for line in merged_seg]
        i = 0
        for line in val_in:
            if re.search(r"\\t\s",line):
                val_out.write(line)
                #remove excessive hyphens by reducing to one. 
                current_b = b_lines[i]
                current_bm = merged_lines[i]
                val_out.write(re.sub(r"-+","-",current_b))
                val_out.write(re.sub(r"-+","-",current_bm))
                i+=1
            else:
                val_out.write(line)

    #add \b annotation to test (covered val) data
    with (open(test_file,"r",encoding="utf-8") as test_in,
          open(f"seg_data/data/{language}/{language_code}-dev-track1-covered","w",encoding="utf-8") as test_out,
          open(f"seg_data/raw/raw_bpe_val.{language_code}.txt","r",encoding="utf-8") as bpe_seg,
          open(f"seg_data/raw/merged_bpe_val.{language_code}.txt","r",encoding="utf-8") as merged_seg):
        #replace inner word w dashes and merge everything as if they were morphemes; add "\b" flag
        b_lines = ["\\b "+re.sub("@@ ","-",line) for line in bpe_seg]
        merged_lines = ["\\q "+re.sub("@@ ","-",line) for line in merged_seg]
        i = 0
        for line in test_in:
            if re.search(r"\\t\s",line):
                test_out.write(line)
                #remove excessive hyphens by reducing to one. 
                current_b = b_lines[i]
                current_bm = merged_lines[i]
                test_out.write(re.sub(r"-+","-",current_b))
                test_out.write(re.sub(r"-+","-",current_bm))
                i+=1
            else:
                test_out.write(line)

    #add \b annotation to "true test" data (covered test)
    with (open(true_test,"r",encoding="utf-8") as ttest_in,
          open(f"seg_data/data/{language}/{language_code}-test-track1-covered","w",encoding="utf-8") as ttest_out,
          open(f"seg_data/raw/raw_bpe_test.{language_code}.txt","r",encoding="utf-8") as bpe_seg,
          open(f"seg_data/raw/merged_bpe_test.{language_code}.txt","r",encoding="utf-8") as merged_seg):
        #replace inner word w dashes and merge everything as if they were morphemes; add "\b" flag
        b_lines = ["\\b "+re.sub("@@ ","-",line) for line in bpe_seg]
        merged_lines = ["\\q "+re.sub("@@ ","-",line) for line in merged_seg]
        i = 0
        for line in ttest_in:
            if re.search(r"\\t\s",line):
                ttest_out.write(line)
                #remove excessive hyphens by reducing to one. 
                current_b = b_lines[i]
                current_bm = merged_lines[i]
                ttest_out.write(re.sub(r"-+","-",current_b))
                ttest_out.write(re.sub(r"-+","-",current_bm))
                i+=1
            else:
                ttest_out.write(line)

if __name__ == "__main__":
    main()