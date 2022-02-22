import pandas as pd
import os
from pathlib import Path
pd.set_option('display.max_colwidth', 100)

df = pd.DataFrame(None, columns = ['path', 'label'])
train_dir = '../input/data/train/images'
out_path = '새로운 df가 저장될 경로를 넣어주세요'

def age_group(x):
    if x < 30:
        return 0
    elif x < 60:
        return 1
    else:
        return 2

for index, line in enumerate(train_df.iloc):
    for file in list(os.listdir(os.path.join(train_dir, line['path']))):
        if file[0] == '.':
            continue
        if file.split('.')[0] == 'normal':
            mask = 2
        elif file.split('.')[0] == 'incorrect_mask':
            mask = 1
        else:
            mask = 0
        gender = 0 if line['gender'] == 'male' else 1
        data = {
            'path': os.path.join(train_dir, line['path'], file),
            'label': mask * 6 + gender * 3 + age_group(line['age'])
        }
        df = df.append(data, ignore_index=True)

df.to_csv(out_path)