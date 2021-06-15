# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:38:41 2021

@author: Casper
"""

class Client():
    """
        Gradient average
    """
    def __init__(self, model, data, scaler=None):
        self.model = model
        self.data = data
        self.scaler = scaler

    def learn(self):
        x = self.data.load_input()
        if(self.scaler.active):
            x = self.scaler.scale(x)
        y_pred = self.data.load_target()
        df_dx = self.model.gradient(x, y_pred)
        return df_dx
    
    def calc_loss(self):
        x = self.data.load_input()
        if(self.scaler.active):
            x = self.scaler.scale(x)
        y_true = self.data.load_target()
        return self.model.loss(x, y_true)
    
    def calc_acc(self):
        x = self.data.load_input()
        if(self.scaler.active):
            x = self.scaler.scale(x)
        y_true = self.data.load_target()
        return self.model.predict_cat(x, y_true)
    
    def setWeights(self, weights):
        self.model.set_weights(weights)
        
        