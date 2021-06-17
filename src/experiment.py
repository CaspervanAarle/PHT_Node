# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:54:48 2021

@author: Casper
"""

import json
import os
import time
import subprocess
import glob



# SHOULD EDIT:
dataset = "readmission_hospital_federated"
data_loc = "C:\\Users\\Casper\\Projects\\MasterScriptie\\custom_projects\\editing\\PHT_Synth_Data_Gen\\out"
nodes_amount = 10

STATIC_LOCKER_PORT = 5050

LEARNCONFIG_NAME = "experiment4"
SETTINGS_LOC = os.getcwd() + "\\..\\settings\\"
MAX_VIRTUAL_MEMORY = 10 * 1024 * 1024 # 10 MB
DATA_DIR = data_loc + "\\{}\\".format(dataset) + "{}.csv"

def generate_json_lockers():
    for filename in glob.glob(SETTINGS_LOC + "locker_*"):
        os.remove(filename) 
    
    config_file = SETTINGS_LOC + "locker_{}.json"
    for i in range(nodes_amount):
        config_file.format(str(i+1))
        out = {'config_name': "locker_" + str(i+1), "host_port": str(STATIC_LOCKER_PORT+i), "csv_location": DATA_DIR.format(str(i+1))}
        with open(config_file.format(str(i+1)),'w') as f:
            json.dump(out, f)

def start_json_lockers():
    for file in os.listdir(SETTINGS_LOC):
        if file.startswith("locker"):
            time.sleep(0.10)
            subprocess.run('start python main.py -c {} -l learnconfig_{}.json'.format(file, LEARNCONFIG_NAME), shell=True)
    
    
if dataset == "PLACEHOLDER" or data_loc == "PLACEHOLDER":
    print("[ERROR] no data location given.")
generate_json_lockers()
start_json_lockers()