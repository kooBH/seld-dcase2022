"""
copy FSD50K data with DCASE category to 
destination directory constructed like

FSD50K/FSD50K.dev_audio/
      /FSD50K.eval_audio/
with
    FSD50K/FSD50K.metadata/collection/collection_dev.csv
    FSD50K/FSD50K.metadata/collection/collection_eval.csv
->
<dest>/0/
       1/
       2/
       ...
       12/
       13/
"""

import pandas as pd
import os
import shutil
from tqdm import tqdm

# Must be '/' at the end of the path

dir_dest = "/home/data/kbh/DCASE2022/"
path_FSD50K = "/home/data/kbh/FSD50K/"
root_dev = path_FSD50K+"FSD50K.dev_audio/"
root_eval = path_FSD50K+"FSD50K.eval_audio/"
csv_dev  = "/home/data/kbh/FSD50K/FSD50K.metadata/collection/collection_dev.csv"
csv_eval = "/home/data/kbh/FSD50K/FSD50K.metadata/collection/collection_eval.csv"



category=[
    ["Female_speech_and_woman_speaking"],
    ["Male_speech_and_man_speaking"],
    ["Clapping"],
    ["Telephone"],
    ["Laughter"],
    ["Vacuum_cleaner","Boiling","Air_conditioning","Mechanical_fan"],
    ["Walk_and_footsteps"],
    ["Door","Cupboard_open_or_close"],
    ["Music"],
    ["Piano","Guitar","Electric_piano","Acoustic_guitar","Cowbell","Marimba_and_xylophone","Rattle_(instrument)"],
    ["Water_tap_and_faucet"],
    ["Bicycle_bell","Doorbell"],
    ["Knock"]
]

""" NOTE
    ~~Bell~~ : 교회 종 소리임  
    ~~Chime~~ : 음이 너무 많음  
 
"""

pd_dev = pd.read_csv(csv_dev)
pd_eval = pd.read_csv(csv_eval)

os.makedirs(dir_dest,exist_ok=True)
for i in range(13) : 
    os.makedirs(dir_dest+"/"+str(i),exist_ok=True)

for i in tqdm(range(len(category))):
    for target in category[i] :
        # Dev
        list_target = pd_dev.loc[pd_dev['labels']==target].fname.tolist()

        for j in list_target : 
            shutil.copy(root_dev+str(j)+".wav", dir_dest+str(i)+"/FSD50K_dev_"+str(j)+".wav")

        # Eval
        list_target = pd_eval.loc[pd_eval['labels']==target].fname.tolist()

        for j in list_target : 
            shutil.copy(root_eval+str(j)+".wav", dir_dest+str(i)+"/FSD50K_eval_"+str(j)+".wav")


