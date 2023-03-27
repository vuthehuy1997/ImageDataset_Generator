
# import tqdm
import os
import shutil
import cv2 
from collections import OrderedDict

path = './aug_trc'

save_path = './aug_trc'
if not os.path.exists(save_path):
    os.makedirs(save_path, exist_ok=True)
out_labels = os.path.join(save_path, 'labels_split.txt')


labels_path = os.path.join(path, 'labels.txt')
dic = {}
with open(labels_path, "r", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        filename, label = line.split('\t')[0], ' '.join(line.split('\t')[1:])
        class_name = filename.split('_')[2]
        if class_name not in dic:
            dic[class_name] = [(filename, label)]
        else:
            dic[class_name].append((filename, label))
    
for k in dic:
    print(k, len(dic[k]))
    leng = len(dic[k])

dic = OrderedDict(sorted(dic.items(), key=lambda t: int(t[0])))
with open(out_labels, "w", encoding="utf8") as f:
    for i in range(leng):
        for k in dic:
            val = dic[k][i]
            f.write(val[0] + '\t' + val[1])
    
    

        
 
