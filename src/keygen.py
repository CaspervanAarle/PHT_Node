# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:42:44 2021

@author: Casper
"""


# homomorphic encryption
from phe import paillier
import os
import pickle



def create_keys():
    public_key, private_key = paillier.generate_paillier_keypair()
    
    # Step 2
    path = '..//enc'
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed, already exists?" % path)
    else:
        print ("Successfully created the directory %s " % path)
        
    with open(path + '//public', 'wb') as config_dictionary_file:
        pickle.dump(public_key, config_dictionary_file)
    with open(path + '//private', 'wb') as config_dictionary_file:
        pickle.dump(private_key, config_dictionary_file)
        
def load_keys():
    with open('..//enc//public', 'rb') as f:
        public_key = pickle.load(f)
    with open('..//enc//private', 'rb') as f:
        private_key = pickle.load(f)
    return public_key, private_key
        

if __name__ == "__main__":
    create_keys()
    load_keys()