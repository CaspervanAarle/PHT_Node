
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:54:57 2021

@author: Casper
"""
import sys
current_module = sys.modules[__name__]

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
    print("private and public key must first be generated before distribution and execution.")
    print("... But for new, we create the keys")
    keygen.create_keys()
    public_key, private_key = keygen.load_keys()
     
     
# ADJUSTABLE PARAMETERS:
HOST = "192.168.0.24"

def learning_loop():
    config, learn_config = config_setup.setup()
    print(str(config).replace(', ',',\n '))
    print(str(learn_config).replace(', ',',\n '))
    
    # load data
    data = Data(config["csv_location"], learn_config["target_list"], learn_config["var_list"])
    
    model_class = getattr(current_module, learn_config["regressor"]) 
    model = model_class([len(learn_config["var_list"])])
    
    if(learn_config["standardization"]):
        scaler = DataScaler()
    else:
        scaler = None
    
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