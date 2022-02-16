import os
import json


def input_scaling(dir, scale):
    file = open(dir, 'r', encoding='UTF-8')
    data = json.load(file)
    name_dir, ext = os.path.splitext(dir)
    for i in range(len(data["images"])):
        data["images"][i]["height"] *= scale
        data["images"][i]["width"] *= scale
    for i in range(len(data["annotations"])):
        data["annotations"][i]["area"] *= scale*scale
        data["annotations"][i]["bbox"] = [x *
                                          scale for x in data["annotations"][i]["bbox"]]
    file_write = open(name_dir + '_edit' + ext, 'w')
    json.dump(data, file_write)
    file.close()
    file_write.close()


# main
json_dir = "Research/annotation_formatting/input_scaling/crack_all.json"
scale_factor = 4
input_scaling(json_dir, scale_factor)
