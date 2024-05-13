import argparse
import re
import csv
import json


def getargs():
    parser = argparse.ArgumentParser("Script for optimizing BPE-MR")

    parser.add_argument("--model_file", required=True)
    parser.add_argument("--freq_file", required=True)
    parser.add_argument("--merge", required = True)

    return parser.parse_args()



def get_last_merge(line):
    #get rid of new line + spaces in between character
    line = re.sub(r'\s','',line)

    if "</w>" in line:
        line = re.sub("</w>",'',line)
    else:
        line = line + "@@"

    return line


def edit_grads(grad_list, current_grad, merge):
    if len(grad_list) < 7:
        grad_list[merge] = current_grad
    else:
        #remove lowest merge item with some conversions between str and int to deal with json 
        del(grad_list[str(min(map(int,grad_list.keys())))])
        grad_list[merge] = current_grad
    return grad_list


def stop(grad_list):
    val = list(grad_list.values())
    bool_val = [True if item in [0,-1] else False for item in val]
    return all(bool_val)


def main(model,freq ,merge, iso):
    #open model file
    with open(model, "r",encoding = "utf-8") as m:
        i = 0
        for line in m:
            #get the last merge operation
            if i == int(merge):
                last_merge = get_last_merge(line)
            else:
                i+=1

    with open(freq, "r",encoding="utf-8") as f:
        freq_reader = csv.reader(f,delimiter="\t")
        for row in freq_reader:
            if row[0] == last_merge:
                current_freq = int(row[1])
                break
    #Get the last freq 
    if merge>1:
        with open(f"./temp_storage/merge_freq.{iso}","r",encoding = "utf-8") as frequencies:
            last_freq = int(frequencies.read())
        grad = current_freq - last_freq

        with open(f"./temp_storage/merge_grad.{iso}","r",encoding="utf-8") as all_grads:
            grad_list = json.load(all_grads)
    else:
        #If in the first merge, just say the grad is the frequency of the first merge
        grad = current_freq
        grad_list = {int(merge): grad}

    #Overwrite the last frequency with the current one for use in the next merge
    with open(f"./temp_storage/merge_freq.{iso}","w",encoding = "utf-8") as frequencies:
        frequencies.write(str(current_freq))
    
    #Write the dif of this and the last freq to a "gradient" file
    grad_list = edit_grads(grad_list, grad, int(merge))

    if len(grad_list)==7:
        #Chekc if all val in list are 0 or -1
        print(stop(grad_list))

    with open(f"./temp_storage/merge_grad.{iso}","w",encoding="utf-8") as all_grads:
        json.dump(grad_list, all_grads, indent = 1, ensure_ascii=False)

if __name__ == "__main__":
    args = getargs()
    iso = args.model_file.split("/")[1].split(".")[-3]
    main(args.model_file,args.freq_file, int(args.merge),iso)

