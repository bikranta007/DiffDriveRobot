# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:49:17 2018

@author: Zhuo Chen
"""
import numpy as np

class Data():
    def __init__(self, robot):
        self.robot = robot
        self.epi_starts = np.array([], dtype = np.bool)
        self.observations = np.zeros((0, self.robot.hPix * self.robot.wPix), dtype = np.int8)
        self.obs2 = np.zeros((0, 3), dtype = np.float32)
        self.actions = np.zeros((0, 2), dtype = np.float32)
    
    def append(self, data2):
        self.epi_starts = np.append(self.epi_starts, data2.epi_starts)
        self.observations = np.append(self.observations, 
                              data2.observations, 
                              axis = 0)
        self.obs2 = np.append(self.obs2, data2.obs2, axis = 0)
        self.actions = np.append(self.actions, data2.actions, axis = 0)
    
    def store(self):
        i = self.robot.index
        np.savez('data/data'+str(i), 
                 epi_starts = self.epi_starts,
                 observations = self.observations,
                 obs2 = self.obs2, 
                 actions = self.actions)
        