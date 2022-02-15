import os
import json
from tqdm import tqdm


def extpaircheck(dir, ext1, ext2):
    for myfile in tqdm(os.listdir(dir)):
        name, ext = os.path.splitext(myfile)
        if ext == ext1:
            expected = name + ext2
            if expected not in os.listdir(dir):
                print("{0} doesn't have {1} pair".format(myfile, ext2))
                os.remove(dir + '/' + myfile)
        elif ext == ext2:
            expected = name + ext1
            if expected not in os.listdir(dir):
                print("{0} doesn't have {1} pair".format(myfile, ext1))
                os.remove(dir + '/' + myfile)


def classcheck(dir):
    for myfile in tqdm(os.listdir(dir)):
        if myfile.endswith(".json"):

            file = open(dir + "/" + myfile, encoding="utf-8")
            try:
                data = json.load(file)
                for i in range(len(data["shapes"])):
                    if data["shapes"][i]["label"] == "mixetruck":
                        data["shapes"][i]["label"] = "mixertruck"
                        print("changed (mixetruck) => (mixertruck)")
                    elif data["shapes"][i]["label"] == "mixtruck":
                        data["shapes"][i]["label"] = "mixertruck"
                        print("changed (mixtruck) => (mixertruck)")
                    # Add if any class misname errors exiest
                    # elif data["shapes"][i]["label"] == "mixtruck":
                    #     data["shapes"][i]["label"] = "mixertruck"
                    #     print("changed (mixtruck) => (mixertruck)")
                file_write = open(dir + "/" + myfile, 'w')
                json.dump(data, file_write)
            except:
                print("error")
                print(myfile)


def dircheck(dir):
    for myfile in tqdm(os.listdir(dir)):
        if myfile.endswith(".json"):
            file = open(dir + "/" + myfile, encoding="utf-8")
            try:
                data = json.load(file)
                if "\\" in data["imagePath"]:
                    fixed_dir = data["imagePath"].replace("\\", "/")
                    final_dir = os.path.basename(fixed_dir)
                    print("{0} => {1}".format(data["imagePath"], final_dir))
                    data["imagePath"] = final_dir
                file_write = open(dir + "/" + myfile, 'w')
                json.dump(data, file_write)
            except:
                print("JSON decode error")
                print(myfile)


# main
file_directory = "Research/annotation_formatting/complete"
extpaircheck(file_directory, ".json", ".png")
classcheck(file_directory)
dircheck(file_directory)
