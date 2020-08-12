import os, shutil
import json
from tqdm import tqdm

_dir_ = 'data/vision/billf/scratch/ruidongwu/data/data_v0'
dst_dir = 'data/vision/billf/scratch/ruidongwu/data/partnet/default'

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

to_move = os.listdir(_dir_)
for num in tqdm(to_move):
    to_move_dir = os.path.join(_dir_,num)
    if os.path.isdir(to_move_dir):
        with open(os.path.join(to_move_dir,'meta.json'),'r') as r:
            model_cat = json.load(r)['model_cat']
        to_dst_dir = os.path.join(dst_dir,model_cat,num)
        if not os.path.exists(to_dst_dir):
            os.makedirs(to_dst_dir)

        shutil.copyfile(os.path.join(to_move_dir,'parts_render','0.png'),os.path.join(to_dst_dir,'0.png'))