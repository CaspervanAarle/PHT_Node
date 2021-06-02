# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:54:48 2021

@author: Casper
"""

import json
import os
import time
import subprocess
import os, glob

# data to use
dataset = "CASP"

# amount of pds's involved (accounts for first x datapoints)
NODES_AMOUNT = 100
SETTINGS_LOC = "C:\\Users\\Casper\\Projects\\MasterScriptie\\custom_projects\\model_training\\PHT_Client\\settings\\"
MAX_VIRTUAL_MEMORY = 10 * 1024 * 1024 # 10 MB



def generate_json_lockers():
    for filename in glob.glob(SETTINGS_LOC + "locker_*"):
        os.remove(filename) 
    data_file = "C:\\Users\\Casper\\Projects\\MasterScriptie\\custom_projects\\model_training\\PHT_data_generator2\\{}_federated\\".format(dataset) + "{}.csv"
    config_file = SETTINGS_LOC + "locker_{}.json"
    for i in range(NODES_AMOUNT):
        config_file.format(str(i+1))
        out = {'config_name': "locker_" + str(i+1), "host_port": str(5050+i), "csv_location": data_file.format(str(i+1))}
        with open(config_file.format(str(i+1)),'w') as f:
            json.dump(out, f)
            


def start_json_lockers():
    for file in os.listdir(SETTINGS_LOC):
        if file.startswith("locker"):
            time.sleep(0.10)
            subprocess.run('start python main.py -c {}'.format(file), shell=True)
            #subprocess.run('start python test.py', shell=True)
            #subprocess.run('start python test.py', shell=True)
            #os.system("start /B start cmd.exe @cmd /k \"cd {} & python nmain.py -c {}\"".format(CODE_LOC + "\\src", file))
    

generate_json_lockers()
start_json_lockers()