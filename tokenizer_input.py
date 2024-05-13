import argparse
import os
import re

def get_args():
    args = argparse.ArgumentParser()

    args.add_argument("--language",choices=["arp","git","lez","ntu","nyb","ddo","usp"],
                      required = True)
    
    return args.parse_args()


def main():

    args = get_args()

    os.makedirs("./tokenizer_in_corp",exist_ok=True)

    language_code_mapping = {
        "arp": "Arapaho",
        "git": "Gitksan",
        "lez": "Lezgi",
        "ntu": "Natugu",
        "nyb": "Nyangbo",
        "ddo": "Tsez",
        "usp": "Uspanteko",
    }
    train_file = f"./data/{language_code_mapping[args.language]}/{args.language}-train-track1-uncovered"
    validation_file = f"./data/{language_code_mapping[args.language]}/{args.language}-dev-track1-uncovered"
    true_test = f"./data/{language_code_mapping[args.language]}/{args.language}-test-track1-covered"
    #Get train data
    with open(train_file,"r",encoding="utf-8") as in_train, open(f"./tokenizer_in_corp/{args.language}_train.txt","w",encoding="utf-8") as out_train:
        for line in in_train:
            if re.search(r"\\t\s",line):
                out_train.write(re.sub(r"\\t\s","",line))
    
    #Get val data
    with open(validation_file,"r",encoding="utf-8") as in_val, open(f"./tokenizer_in_corp/{args.language}_val.txt","w",encoding="utf-8") as out_val:
        for line in in_val:
            if re.search(r"\\t ",line):
                out_val.write(re.sub(r"\\t ","",line))

    #Get test data
    with open(true_test,"r",encoding="utf-8") as in_test, open(f"./tokenizer_in_corp/{args.language}_test.txt","w",encoding="utf-8") as out_test:
        for line in in_test:
            if re.search(r"\\t ",line):
                out_test.write(re.sub(r"\\t ","",line))


if __name__ == "__main__":
    main()