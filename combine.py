
from tqdm import tqdm
import os
import shutil
import cv2 
import imghdr

path = './gen_image/visa'

save_path = './gen_image/visa_v1'
if not os.path.exists(save_path):
    os.makedirs(save_path, exist_ok=True)
out_labels = os.path.join(save_path, 'labels.txt')
file_labels = open(out_labels, "w", encoding="utf8")

list_dir = os.listdir(path)

for cate in list_dir:

    folder = os.path.join(path, cate)

    labels_path = os.path.join(folder, 'labels.txt')
    with open(labels_path, "r", encoding="utf8") as f:
        lines = f.readlines()
        for i in tqdm(range(len(lines))):
            line = lines[i]
            filename, label = line.split('\t')[0], ' '.join(line.split('\t')[1:])
            file_labels.write(cate + '_' + filename + '\t' + label)
            in_path  = os.path.join(folder, filename)
            out_path = os.path.join(save_path, cate + '_' + filename)
            shutil.copyfile(in_path, out_path)

file_labels.close()
    
    

        
 
