#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:33:18 2022

@author: master
"""

def shape_data_exo(y_train_exo):
    """
    fonction qui redimensionne les données de sorties exogénes
    entrées:
        y_train_exo:les données de sortie exogénes
    sorties:
    y_train_exo_ohog: données de sortie exogénes train pour la caractéristique 'genre' de dimension (n*3)
    y_train_exo_ohor: données de sortie exogénes train pour la caractéristique 'race' de dimension (n*3)
    y_train_exo_ohoa: données de sortie exogénes train pour la caractéristique 'age' de dimension (n*5)
    y_test_exo_ohog: données de sortie exogénes test pour la caractéristique 'genre' de dimension (n*3)
    y_test_exo_ohor: données de sortie exogénes test pour la caractéristique 'race' de dimension (n*3)
    y_test_exo_ohoa: données de sortie exogénes test pour la caractéristique 'age' de dimension (n*5)
    """
    
#------------------------ sorties train---------------------------------------------

    y_train_exo_ohog=[] # sorties exogénes train pour le genre
    y_train_exo_ohor=[] # sorties exogénes train pour la race
    y_train_exo_ohoa=[] # sorties exogénes train pour l'age
    
    for i in range (len(y_train_exo)): 
        g=y_train_exo[i][0]
        r=y_train_exo[i][1]
        a=y_train_exo[i][2]
        
        #genre
        if g==0 : 
            temg= [1,0,0]
        if g==1 :
            temg=[0,1,0]    
        if g==2 :
            temg=[0,0,1]
        
        #race
        if r==0 : 
            temr= [1,0,0]
        if r==1 :
            temr= [0,1,0]
        if r==2 : 
            temr= [0,0,1]
        
        #age
        if a==0 : 
            tema= [1,0,0,0,0]
        if a==1 : 
            tema= [0,1,0,0,0]
        if a==2 : 
            tema= [0,0,1,0,0]
        if a==3 : 
            tema= [0,0,0,1,0]
        if a==4 :
            tema= [0,0,0,0,1]

        y_train_exo_ohog.append(temg)   
        y_train_exo_ohor.append(temr)
        y_train_exo_ohoa.append(tema)

    
    y_train_exo_ohog =np.array(y_train_exo_ohog) 
    y_train_exo_ohor =np.array(y_train_exo_ohor)
    y_train_exo_ohoa =np.array(y_train_exo_ohoa)

#-----------------------------sortie test----------------------------------------

    y_test_exo_ohog=[] # sorties exogénes train pour le genre
    y_test_exo_ohor=[] # sorties exogénes train pour la race
    y_test_exo_ohoa=[] # sorties exogénes train pour l'age
    
    for i in range (len(y_test_exo)): 
        
        #genre
        g=y_test_exo[i][0]
        r=y_test_exo[i][1]
        a=y_test_exo[i][2]
        if g==0 : 
            temg= [1,0,0]
        if g==1 :
            temg=[0,1,0]    
        if g==2 :
            temg=[0,0,1]
        
        #race
        if r==0 : 
            temr= [1,0,0]
        if r==1 :
            temr= [0,1,0]
        if r==2 : 
            temr= [0,0,1]
        
        #age
        if a==0 : 
            tema= [1,0,0,0,0]
        if a==1 : 
            tema= [0,1,0,0,0]
        if a==2 : 
            tema= [0,0,1,0,0]
        if a==3 : 
            tema= [0,0,0,1,0]
        if a==4 :
            tema= [0,0,0,0,1]

        y_test_exo_ohog.append(temg)   
        y_test_exo_ohor.append(temr)
        y_test_exo_ohoa.append(tema)


    y_test_exo_ohog =np.array(y_test_exo_ohog) 
    y_test_exo_ohor =np.array(y_test_exo_ohor)
    y_test_exo_ohoa =np.array(y_test_exo_ohoa)
 
    
    return y_train_exo_ohog,y_train_exo_ohor,y_train_exo_ohoa,y_test_exo_ohog,y_test_exo_ohor,y_test_exo_ohoa