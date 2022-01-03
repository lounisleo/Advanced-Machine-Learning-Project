#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:36:01 2022

@author: master
"""

# Tree gate 
def Tree_gate(y_train_exo):
    """
    cette fonction contient le bloc Tree gate
    les entrées:
        y_train_exo: les données de sortie exogénes train
    les sorties:
        g: les données predites
    """
    tree=DecisionTreeRegressor(max_features="log2",max_depth=5)
    tree.fit(y_train_exo,y_train_exo)
    # make prediction 
    g=tree.predict(y_test_exo)
    
    return g 