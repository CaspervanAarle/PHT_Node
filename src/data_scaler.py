# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:20:59 2021

@author: Casper
"""

class DataScaler():
    def __init__(self, mu=[], sigma=[]):
        self.mu = mu
        self.sigma = sigma
        
    def scale(self, inputs):
        return ( inputs - self.mu ) / self.sigma
    
    def set_mu_sigma(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        
        