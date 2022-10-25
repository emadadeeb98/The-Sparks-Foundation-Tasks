import glob
import os
import numpy as np
import sys

current_dir = "C:/Users/Adeeb/Desktop/Genetic Algorithms/archive/images"
split_pct = 20
file_train = open("C:/Users/Adeeb/Desktop/train.txt", "w")
file_val = open("C:/Users/Adeeb/Desktop/test.txt", "w")
counter = 1
index_test = round(100 / split_pct)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.png")):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        if counter == index_test:
                counter = 1
                file_val.write(current_dir + "/" + title + '.jpg' + "\n")
        else:
                file_train.write(current_dir + "/" + title + '.jpg' + "\n")
                counter = counter + 1
file_train.close()
file_val.close()