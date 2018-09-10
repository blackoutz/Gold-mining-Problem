# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 23:00:48 2018

@author: 58011256
"""
import pandas as pd

def isGold(obj):
    if obj.find('G') > -1:
        profit = obj[int(obj.find('G')+2):int(obj.find(','))]
        return int(profit)

def isCost(obj):
    if obj.find('W') > -1:
        cost = obj[int(obj.find('W')+2):]
        return int(cost)
    
df = pd.read_csv('MiningGameEngine.csv',header = None)
Map = df.iloc[:24,:].values

for i in range(len(Map)):
    for j in range(len(Map[0])):
        for char in Map[i][j]:
            if char in '{}':
                Map[i][j] = Map[i][j].replace(char,'')
            if char == 'S':
                start_index = [i,j]
    
profit = isGold(Map[10,2])
cost = isCost(Map[10,2])