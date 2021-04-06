# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:54:57 2021

@author: Casper
"""

from ipc_server import IPC_Server
from ndatasocket import Data
import config_setup

# import the correct algorithm:
from classifier_methods import LinReg
from aggregate_methods import FedSGD_Client

import time

# DEFAULT GATEWAY, ADJUST TO YOUR OWN
HOST = "192.168.0.13"

def learning_loop():
    config = config_setup.setup()
    
    var_list = ["var_1", "var_2", "var_3", "var_4", "var_5", "var_6"]
    target_list = ["var_9"]
    
    # load data
    data = Data(config["csv_location"], target_list, var_list)
    
    model = LinReg([len(var_list)])
    
    # initialize the locker part of the aggregate method
    aggregator_locker = FedSGD_Client(model, data)
    
    # connect to server
    connection = IPC_Server(HOST, config['host_port'])
    
    while True:
        # receive
        weights = connection.receive_request()
        print("[INFO] Request received")
        
        # execute task
        time.sleep(2)
        model.set_weights(weights)
        derivative = aggregator_locker.learn()
        
        # send
        connection.respond(derivative)
        print("[INFO] Request ended")
 
    
if __name__ == "__main__" :
    learning_loop()