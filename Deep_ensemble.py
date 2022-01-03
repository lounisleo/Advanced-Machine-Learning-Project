#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:26:55 2022

@author: master
"""

def Deep_ensemble(y_train_endo):
    """
    cette fonction contient le classifieur deep ensemble
    les entrées:
        y_train_endo: données de sortie endogénes 
    les sorties:
        y_pred:les données predites par le classifieur adaboost
    """
    y_endo=np.reshape(y_train_endo,(np.shape(y_train_endo)[0],1))
    clf = AdaBoostClassifier(n_estimators=32)
    model = clf.fit(y_endo,y_train_endo)
    y_pred=model.predict(y_endo)
    
    return y_pred
