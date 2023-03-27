
# import tqdm
import os
import shutil
import cv2 
from collections import OrderedDict

path = './aug_trc_other/labels.txt'

# save_path = './gen_33/vietocr_.txt'

labels = []
with open(path, "r", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        # filename, label = line.split('\t')[0], ' '.join(line.split('\t')[1:])
        a = line.split('\t')
        if len(a) != 2:
            print(line)

        # labels.append(label)

# with open(save_path, "w", encoding="utf8") as f:
#     for i in labels:
#         f.write(i)
    
    

        
 
