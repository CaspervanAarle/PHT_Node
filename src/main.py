
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:54:57 2021

@author: Casper
"""

from ipc_server import IPC_Server
from ndatasocket import Data
import config_setup
import math

# import the correct algorithm:
from classifier_methods import LinReg, LogReg
from aggregate_methods import FedSGD_Client
from data_scaler import DataScaler
import keygen

# homomorphic encryption
from phe import paillier
try:
    public_key, private_key = keygen.load_keys()
except Exception:
    keygen.create_keys()
    public_key, private_key = keygen.load_keys()
     
     
# ADJUSTABLE PARAMETERS:
HOST = "192.168.0.24"
model_class = LinReg
#var_list = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]
#target_list = ["RMSD"]
#var_list = ["doc-avail", "hosp_avail", "income_1000s", "pop_density"]
#target_list = ["death_rate_per_1000"]
var_list = ["age", "bmi", "children"]
target_list = ["charges"]
#var_list = ["time_in_hospital",	"num_lab_procedures",	"num_procedures",	"num_medications",	"number_outpatient",	"number_emergency",	"number_inpatient",	"number_diagnoses"]
#target_list = ["readmitted"]
#var_list = ["Age",	"BMI"	,"Glucose",	"Insulin"	,"HOMA",	"Leptin",	"Adiponectin",	"Resistin"	,"MCP.1"]
#target_list = ["Classification"]
#var_list =  ["age",	"operation_year",	"nodes_detected"]	
#target_list =  ["died_within_5y"]


def learning_loop():
    config = config_setup.setup()
    print(config)
    
    # load data
    data = Data(config["csv_location"], target_list, var_list)
    
    model = model_class([len(var_list)])
    
    scaler = DataScaler()
    #scaler = None
    
    # initialize the locker part of the aggregate method
    aggregator_locker = FedSGD_Client(model, data, scaler)
    
    # connect to server
    connection = IPC_Server(HOST, config['host_port'])
    
    while True:
        
        weights = connection.receive_request()
        print(weights)
        if weights[2] == 0:
            print("[INFO] Validation request received")
            model.set_weights((weights[0], weights[1]))
            loss = aggregator_locker.calc_loss()
            connection.respond(loss)
            print("[INFO] Validation request ended")
          
        if weights[2] == 1:
            print("[INFO] Request received")
            model.set_weights(weights)
            derivative = aggregator_locker.learn()
            connection.respond(derivative)
            print("[INFO] Request ended")
            
        if weights[2] == 2:
            print("[INFO] Accuracy request received")
            model.set_weights((weights[0], weights[1]))
            accuracy = aggregator_locker.calc_acc()
            connection.respond(accuracy)
            print("[INFO] Accuracy request ended")
            
        if weights[2] == 3:
            print("[INFO] Encrypted mean request received")
            values = data.load_input()[0]
            enc_data = [public_key.encrypt(x) for x in values]
            connection.respond(enc_data)
            print("[INFO] Encrypted mean request ended")
        if weights[2] == 4:
            print("[INFO] Encrypted mean request 2 received")
            means_sq = [private_key.decrypt(x) for x in weights[0]]
            means = [math.sqrt(x) for x in means_sq]
            print("means received: {}".format(means))
            connection.respond("")
            print("[INFO] Encrypted mean request 2 ended")
            
            
        if weights[2] == 5:
            print("[INFO] Encrypted stdev request received")
            values = data.load_input()[0] - means
            print(values)
            enc_data = [public_key.encrypt(x**2) for x in values]
            connection.respond(enc_data)
            print("[INFO] Encrypted stdev request ended")
        if weights[2] == 6:
            print("[INFO] Encrypted stdev request 2 received")
            stdevs = [private_key.decrypt(x) for x in weights[0]]
            print("stdevs received: {}".format(stdevs))
            if(scaler):
                scaler.set_mu_sigma(means, stdevs)
            connection.respond("")
            print("[INFO] Encrypted stdev request 2 ended")
    
if __name__ == "__main__" :
    learning_loop()