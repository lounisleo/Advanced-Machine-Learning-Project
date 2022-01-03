#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:24:20 2022

@author: master
"""

## application du one hot encoding pour la representation endogene 
def data_endo(y_train_endo,y_test_endo):
    """
    cette fonction redimensionne les données endogene
    entrées:
        y_train_endo:données de sortie endogenes train de dimension (n*1)
        y_test_endo:données de sortie endogenes test de dimension (n*1)
    sorties:
    ytrain_end :données de sortie endogenes train de dimension (n*7)
    ytest_end: données de sortie endogenes test de dimension (n*7)
    
    """
    ytrain_end, ytest_end = [],[] 
    
    #-----------------train--------------------------------------
    for i in range(len(y_train_endo)):
        if y_train_endo[i]==1:
            ytrain_end.append([0,0,0,0,0,0,1])
        if y_train_endo[i]==2:
            ytrain_end.append([0,0,0,0,0,1,0])
        if y_train_endo[i]==3:
            ytrain_end.append([0,0,0,0,1,0,0])
        if y_train_endo[i]==4:
            ytrain_end.append([0,0,0,1,0,0,0])
        if y_train_endo[i]==5:
            ytrain_end.append([0,0,1,0,0,0,0])
        if y_train_endo[i]==6:
            ytrain_end.append([0,1,0,0,0,0,0])
        if y_train_endo[i]==7:
            ytrain_end.append([1,0,0,0,0,0,0])
            
    #-----------------test-----------------------------------------
    for i in range (len(y_test_endo)):
        if y_test_endo[i]==1:
            ytest_end.append([0,0,0,0,0,0,1])
        if y_test_endo[i]==2:
            ytest_end.append([0,0,0,0,0,1,0])
        if y_test_endo[i]==3:
            ytest_end.append([0,0,0,0,1,0,0])
        if y_test_endo[i]==4:
            ytest_end.append([0,0,0,1,0,0,0])
        if y_test_endo[i]==5:
            ytest_end.append([0,0,1,0,0,0,0])
        if y_test_endo[i]==6:
            ytest_end.append([0,1,0,0,0,0,0])
        if y_test_endo[i]==7:
            ytest_end.append([1,0,0,0,0,0,0])

    ytrain_end = np.array(ytrain_end)
    ytest_end = np.array(ytest_end)

    return ytrain_end,ytest_end