# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:45:40 2021

@author: Casper
"""
import random
import pyDH
import numpy as np

class DHGenerator():
    def __init__(self):
        self.d1 = pyDH.DiffieHellman()   
        self.d1_pubkey = None
        
    def generate_key(self):
        self.d1_pubkey = self.d1.gen_public_key()
        return self.d1_pubkey
        
    def generate_shared_keys(self, public_key_list):
        self.index = public_key_list.index(self.d1_pubkey)
        public_key_list.remove(self.d1_pubkey)
        self.shared_keys = [self.d1.gen_shared_key(key) for key in public_key_list]
        
    def mask_weights(self, weights):
        for i, shared_key in enumerate(self.shared_keys):
            random.seed(shared_key)
            mask = [random.random()*1E7 if i < self.index else -random.random()*1E7 for w in weights]
            #print(mask)
            weights = [x + y for x, y in zip(weights, mask)]
        return weights
    
    
    