# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:38:41 2021

@author: Casper
"""

class FedAvg_Client():
    """
        Model average
    """
    def __init__(self, model, data):
        self.model = model
        self.agg_type = "FedAvg"
        self.BATCH_SIZE = 8
        self.EPOCHS = 10

    def learn(self):
        pass
    
    def setWeights(self, weights):
        self.model.set_weights(weights)
        
        
class FedSGD_Client():
    """
        Gradient average
    """
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def learn(self):
        x = self.data.load_input()
        y_pred = self.data.load_target()
        df_dx = self.model.gradient(x, y_pred)
        return df_dx
    
    def setWeights(self, weights):
        self.model.set_weights(weights)