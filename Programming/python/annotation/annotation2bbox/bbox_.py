import json
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import pandas as pd


def drawbbox_dir(dir, thickness=2, mode="withlabel"):
    pbar = tqdm(total=len(os.listdir(dir)))
    for myfile in os.listdir(dir):
        file_name, file_ext = os.path.splitext(myfile)
        if file_ext == ".json":  # myfile = filename.ext
            name_dir = dir + "/" + file_name
            drawbbox(name_dir, thickness=thickness, mode=mode)
        pbar.update(1)
    pbar.close()


def drawbbox(name_dir, thickness=2, mode="withlabel"):
    class_dict = {"worker":1, "hardhat":2, "harness":3, "strap":4, "hook":5}
    font = cv2.FONT_HERSHEY_SIMPLEX
    json_dir = name_dir + ".json"
    png_dir = name_dir + ".png"
    # txt_dir = name_dir + ".txt"
    dir, name_png = os.path.split(png_dir)
    image = cv2.imread(png_dir)
    image_width = np.shape(image)[1]
    image_height = np.shape(image)[0]
    json_file = open(json_dir)
    json_data = json.load(json_file)  # loads json as dictionary
    shapes = json_data["shapes"]  # type(shapes) = list of all the objects
    colordict = {}
    color = (0, 0, 255)
    outpath = 'bbox/'+dir
    os.makedirs(outpath, exist_ok=True)
    outname = outpath + "/" + name_png
    txt_path, ext = os.path.splitext(outname)
    f = open(txt_path+".txt", 'w')
    for obj in shapes:  # obj is dictionary of obj annotation information

        obj_label = obj["label"]  # class name
        obj_pointarray = np.array(obj["points"])  # (N, 2) numpy array

        if obj_label in colordict:
            color = colordict[obj_label]
        else:
            color = tuple(np.random.random(size=3) * 256)
            colordict[obj_label] = color

        max = np.amax(obj_pointarray, axis=0)
        min = np.amin(obj_pointarray, axis=0)
        max_int = max.astype(int) # np array (2,1)
        min_int = min.astype(int) # np array (2,1)
        cv2.rectangle(image, min_int, max_int, color, thickness)

        bbox_size = np.subtract(max_int, min_int)
        bbox_width = bbox_size[0]
        bbox_height = bbox_size[1]
        full_mat = np.vstack((min, max))

        center_mat = np.mean(full_mat, axis=0)

        x_c = center_mat[0]
        y_c = center_mat[1]

        txt_line = "{0} {1} {2} {3} {4}\n".format(class_dict[obj_label], x_c/image_width, y_c/image_height, bbox_width/image_width, bbox_height/image_height)
        f.write(txt_line)        

        #cv2.circle(image, (int(x_c), int(y_c)), 0, color, thickness)
        # max_min = np.concatenate((min_int, max_int), axis=1)
        # df = pd.DataFrame(max_min, columns=["min", "max"])
        # with open("np.txt", 'a') as f:
        #     dfAsString = df.to_string(header=True, index=False)
        #     f.write(dfAsString)


        if mode == "withlabel":
            text_size, _ = cv2.getTextSize(obj_label, font, 1, 2)
            text_w, text_h = text_size
            cv2.rectangle(image, (max_int[0], max_int[1]),
                          (max_int[0]+text_w, max_int[1]-text_h), (0, 0, 0), -1)
            cv2.putText(image, obj_label,
                        (max_int[0], max_int[1]), font, 1, color, 1)

    cv2.imwrite(outname, image)
    f.close()



    


 