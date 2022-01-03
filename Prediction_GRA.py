#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:32:38 2022

@author: master
"""

def Prediction_GRA(y_test_exo_ohoGender,y_test_exo_ohoRace,y_test_exo_ohoAge): 
    """
    la fonction permet de prédire la sortie pour chacun des trois caractéristique genre,race et age
    entrées:
        y_test_exo_ohoGender: données de test exogenes pour le genre
        y_test_exo_ohoRace: données de test exogenes pour la race
        y_test_exo_ohoAge: données de test exogenes pour l'age
    """
    
    #chargement des modeles
    Pwd='/home/user/'
    ModelLoadGender = keras.models.load_model(Pwd+'SaveModelgender') 
    ModelLoadRace = keras.models.load_model(Pwd+'SaveModelRace')
    ModelLoadAge = keras.models.load_model(Pwd+'SaveModelAge')
    #predire la sortie 
    y_predGender=ModelLoadGender.predict(x_test)#--------------------------------------------------------------------------- ??????????
    y_predRace=ModelLoadRace.predict(x_test)
    y_predAge=ModelLoadAge.predict(x_test)
    
    ########## Mes 3 vecteurs predit #############

    y_predGender=np.argmax(y_predGender, axis=1)
    y_predRace=np.argmax(y_predRace, axis=1)
    y_predAge=np.argmax(y_predAge, axis=1)
    #############################################

    Y_testGender=np.argmax(y_test_exo_ohoGender, axis=1)
    Y_testRace=np.argmax(y_test_exo_ohoRace, axis=1)
    Y_testAge=np.argmax(y_test_exo_ohoAge, axis=1)
    ###################Confusion Matrix ###########
    
    cm_Gender  = confusion_matrix(Y_testGender, y_predGender)
    cm_Race  = confusion_matrix(Y_testRace, y_predRace)
    cm_Age  = confusion_matrix(Y_testAge, y_predAge)
    ###################### AFFICHAGE #################
    print("taux d'apprentissage du Genre est : ",  accuracy_score(Y_testGender, y_predGender)*100, "%")
    print("cm_Gender = \n", cm_Gender)
    print("la taille de y_predGender : ", np.shape(y_predGender))
    
    print("taux d'apprentissage de la Race est : ",  accuracy_score(Y_testRace, y_predRace)*100, "%")
    print("cm_Race = \n", cm_Race)
    print("la taille de y_predRace : ", np.shape(y_predRace))
    
    print("taux d'apprentissage de l'age est : ",  accuracy_score(Y_testAge, y_predAge)*100, "%")
    print("===== matrice de confusion pour la Var Age ===== \n", cm_Age)
    print("la taille de y_predAge : ", np.shape(y_predAge))
    
    y_pred_exo=[]
    for i in range (len(y_predGender)):
        y_pred_exo.append([y_predGender[i],y_predRace[i],y_predAge[i]])
    
    y_pred_exo=np.array(y_pred_exo)
    return y_pred_exo #return 3 vectors of Y_pred [Gender],[Race], [Age] de taille de 3068