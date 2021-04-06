# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:38:18 2021

@author: Casper
"""
import pandas as pd
import numpy as np

DATA_DIR = ""

class Data():
    def __init__(self, direc, tar_list, var_list=[], is_personal_locker=True):
        self.direc = direc
        self.var_list = var_list
        self.tar_list = tar_list
        self.is_personal_locker=True

    def load_input(self):
        if(self.is_personal_locker):
            if self.var_list == []:
                data = pd.read_csv(self.direc).iloc[0].values.tolist()
            else:
                data = pd.read_csv(self.direc)[self.var_list].iloc[0].values.tolist()
        else:
            # TODO: no personal locker
            pass
        
        return np.array([data])
    
    def load_target(self):
        if(self.is_personal_locker):
            if self.var_list == []:
                data = pd.read_csv(self.direc).iloc[0].values.tolist()
            else:
                data = pd.read_csv(self.direc)[self.tar_list].iloc[0].values.tolist()
        else:
            # TODO: no personal locker
            pass
        
        return data
    