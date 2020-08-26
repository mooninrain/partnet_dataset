import os
import json

root = '/data/vision/billf/scratch/ruidongwu/data/data_v0'
all_dirs = os.listdir(root)
all_nums = []
for _dir_ in all_dirs:
    _path_ = os.path.join(root, _dir_,'result.json')
    with open(_path_,'r') as r:
        data = json.load(r)
        num = len(data[0]['children'])
        all_nums.append(num)
print(max(all_nums))