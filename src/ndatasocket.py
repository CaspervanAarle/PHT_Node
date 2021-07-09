# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:38:18 2021

@author: Casper
"""
import pandas as pd
import numpy as np

class Data():
    def __init__(self, direc, tar_list, var_list=[], is_personal_locker=True):
        self.direc = direc
        self.var_list = var_list
        self.tar_list = tar_list
        self.is_personal_locker=True
        self.data_in = pd.read_csv(self.direc)[self.var_list].iloc[0].values.tolist()
        self.data_out = pd.read_csv(self.direc)[self.tar_list].iloc[0].values.tolist()
        print(self.data_in)
        
        

    def load_input(self):
        return np.array([self.data_in]).astype(float)
    
    def load_target(self):
        return self.data_out
    
    def set_scaled_data(self, x_scaled):
        self.data_in = x_scaled
        print(self.data_in)