#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:35:10 2022

@author: master
"""

def train_model_exogenous(x_train,y_train_endo,y_train_exo):
    """
    Cette fonction lance l'entrainement du model exogéne pour les trois caractéristiques différentes (Genre,Race,Age)
    """
    x_train, x_test, y_train_endo, y_test_endo,y_train_exo,y_test_exo= create_data()
    y_train_exo_ohog,y_train_exo_ohor,y_train_exo_ohoa,y_test_exo_ohog,y_test_exo_ohor,y_test_exo_ohoa=shape_data_exo(y_train_exo)
    
    history_gender=Exogenous_rep(3,x_train,y_train_exo_ohog,'/home/user/SaveModelgender')
    visualise(history_gender)
    
    history_race=Exogenous_rep(3,x_train,y_train_exo_ohor,'/home/user/SaveModelAge')
    visualise(history_race)
    
    history_age=Exogenous_rep(5,x_train,y_train_exo_ohoa,'/home/user/SaveModelRace')
    visualise(history_age)