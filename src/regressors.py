# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:54:33 2021

@author: Casper
"""
import numpy as np


class LinReg():
    def __init__(self, hidden_units):
        self.hidden_units = hidden_units
        self.m = np.random.normal(loc=0.0, scale=1.0, size=hidden_units)
        self.c = 0

    def call(self, inputs):
        return np.dot(inputs, self.m) + self.c

    def gradient(self, X, Y):
        Y_pred = self.call(X)  # The current predicted value of Y=
        D_m = (-2/float(len(X))) * np.dot((Y - Y_pred), X) #+ self.lambda_*2*self.m # Derivative wrt m
        D_c = (-2/float(len(X))) * sum(Y - Y_pred) #+ self.lambda_*2*self.c # Derivative wrt c
        return D_m, D_c

    def loss(self, X, y):
        ''' squared error '''
        return (self.call(X) - y)**2

    def get_weights(self):
        return (self.m, self.c)

    def set_weights(self, value):
        self.m = value[0]
        self.c = value[1]
        return


class LogReg():
    def __init__(self, hidden_units):
        self.hidden_units = hidden_units
        self.m = np.random.normal(loc=0.0, scale=1.0, size=hidden_units)
        self.c = 0
        #self.lambda_ = 0.0001

    def call(self, inputs):
        return self._sigmoid(np.dot(inputs, self.m) + self.c)

    def gradient(self, X, Y):
        Y_pred = self.call(X)
        D_m = np.array(np.dot(X.T, Y_pred - Y)) #+ self.lambda_*2*self.m
        D_c = Y_pred[0] - Y[0] #+ self.lambda_*2*self.c
        return D_m, D_c

    def loss(self, X, y):
        y_pred = self.call(X)
        if y[0] == 1:
            loss = -np.log(y_pred[0])
        else:
            loss = -np.log(1 - y_pred[0])
        return loss

    def predict_cat(self, X, y):
        y_pred = self.call(X)
        return int(round(y_pred[0]) == y[0])

    def get_weights(self):
        return (self.m, self.c)

    def set_weights(self, value):
        self.m = value[0]
        self.c = value[1]
        return

    def _sigmoid(self, x):
        # Activation function used to map any real value between 0 and 1
        return 1 / (1 + np.exp(-x))
