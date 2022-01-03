#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:29:23 2022

@author: master
"""


def Endogenous_rep(x_train,xtest,y_train_endo,y_test_endo,lr=0.0001,batch_size=100,epochs=100):
    """
    modele pour la representation endogénes
    entrées:
        x_train,xtest,y_train_endo,y_test_endo: données d'entrée
    sorties:
        y_pred: données endogénes predites
        model_endo: modele endogéne
        ytest_end: sortie test endogénes
        history: l'historique du modèle
    """
    
    ytrain_end,ytest_end = data_endo(y_train_endo,y_test_endo)
    Vgg_endo = VGG16(input_shape = (100, 100,3),include_top = False,weights = 'imagenet')
    Vgg_endo.trainable=False # to kept only convolution parameters layers froozen 
    # ADD 3 fully connected layers to endogenous representation model
    model_endo=keras.Sequential([Vgg_endo,
    keras.layers.Flatten(),
    keras.layers.BatchNormalization(),  
    keras.layers.Dense(units=4096,activation="relu"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(units=4096,activation="relu"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(units=7,activation="softmax")
    ])
    #tf.keras.losses.CategoricalCrossentropy()
    model_endo.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=lr,name='Adam'),metrics=['accuracy'])
    history = model_endo.fit(x_train,ytrain_end ,batch_size=batch_size,epochs=epochs)
    y_pred=model_endo.predict(x_test)
    y_pred=np.argmax(y_pred, axis=1)

    return y_pred, model_endo,history,ytest_end

def Exogenous_rep(u,x_train,y_train_exo_oho, Save_Path):
    """
    modele pour la representation exogénes
    entrées:
        u : nombres de neuronnes de sortie (5 pour AGE, 3 pour Genre, 3 pour Race )
        y_train_exo_oho : label soit (Age, Genre, Race)
        Save_path: le chemin d'acces ou le modele sera sauvegarder
    sorties:
        history: l'historique du modèle
    """
    
    # Exogenous représentation 
    Vgg_exo = VGG16(input_shape = (100, 100,3),include_top = False,weights = 'imagenet')
    Vgg_exo.trainable=False# to kept only convolution parameters layers froozen 
    model_exo=keras.Sequential([Vgg_exo,
    keras.layers.Flatten(),
    keras.layers.BatchNormalization(),  
    keras.layers.Dense(units=4096,activation="relu"),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(units=4096,activation="relu"),
    keras.layers.BatchNormalization(),
    #keras.layers.Dense(units=3,activation="relu")
    keras.layers.Dense(units=u,activation='softmax') # units = 3 pour gender and race units= 5 pour age
    ])
    model_exo.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001,name='Adam'),metrics=['accuracy'])
    history = model_exo.fit(x_train,y_train_exo_oho ,batch_size=100,epochs=50)

    model_exo.trainable=False
    #Saving a Keras model:
    model_exo.save(Save_Path)
    
    return history