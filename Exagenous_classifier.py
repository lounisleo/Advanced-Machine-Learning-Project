#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:29:59 2022

@author: master
"""


def Exagenous_classifier(y_train_exo,y_train_endo,y_test_endo,y_test_exo,r=0.0001,batch_size=32,epoch=50,loss='mse'):
    """
    la focntion crée le classifieur exagenous 
    les entrées:
        y_train_exo,y_test_exo: les donneés de sortie exogenes train et test
        y_train_endo,y_test_endo: les donneés de sortie endogénes train et test
    les sorties:
        res: 
    """
    inputL = keras.layers.Input(shape=(4,))
    hiddenL = keras.layers.Dense(2,activation='sigmoid')(inputL)
    outputL = keras.layers.Dense(4,activation='linear')(hiddenL)
    autoencoder = keras.models.Model(inputL,outputL)
    
    #crée une entrée du reseau 'y' a partir de 'y_train_exo' de dimension (n*4) -------------------------- a verifier 
    y=[]
    for i in range(len(y_train_exo)):
        a=[]
        for j in range(3):
            a.append(y_train_exo[i][j])
        a.append(y_train_endo[i])
        y.append(a)
        
    autoencoder.compile(loss=loss,optimizer=tf.keras.optimizers.Adam(learning_rate=lr,name='Adam'),metrics=['accuracy'])
    hist=autoencoder.fit(y,y,batch_size=batch_size,epochs=epoch)
    
    #crée une entrée a predire 'z' a partir de 'y_test_exo' de dimension (n*4)------------------------------- a verifier 
    z=[]
    for i in range(len(y_test_exo)):
        a=[]
        for j in range(3):
            a.append(y_test_exo[i][j])
        a.append(y_test_endo[i])
        z.append(a)
    
    res=autoencoder.predict(z)
    
    
    return res