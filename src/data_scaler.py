# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:20:59 2021

@author: Casper
"""

class DataScaler():
    def __init__(self, mu=[], sigma=[]):
        self.mu = mu
        self.sigma = sigma
        self.active = False
        
    def scale(self, inputs):
        x_scale = ( inputs - self.mu ) / self.sigma
        return x_scale
    
    def set_mu_sigma(self, mu, sigma):
        self.active = True
        self.mu = mu
        self.sigma = sigma
        
        
        