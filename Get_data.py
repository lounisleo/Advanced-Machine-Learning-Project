#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:31:35 2022

@author: master
"""

def PrepareDateSet(pathNameLabels,pathNameImg,pathNameLabels_exo):
    """
    fonction pour recupérer la base de données 
    entrées:
        pathNameLabels: chemin d'accés aux données labels endogénes
        pathNameImg:chemin d'accés aux données des images
        pathNameLabels_exo:chemin d'accés aux données labels exogénes
    sorties:
        x_train,x_test:données d'entrées 
        y_train,y_test:données de sorties endogénes
        y_train_exo,y_test_exo : données de sorties exogénes
    """
    y_train=[]
    y_test=[]
    x_train=[]
    x_test=[]
    y_train_exo=[]
    y_test_exo=[]
    
#-------------------------labels_endogens-----------------------------------------  
    with open(pathNameLabels) as f:
        line = f.readline()
        while line:
            if 'train' in line :    
                y_train.append(int(line[16]))
            if 'test' in line : 
                y_test.append(int(line[14]))   

            line = f.readline()
    y_train=np.array(y_train)
    y_test=np.array(y_test)
    
#-------------------------labels_exogens ---------------------------------------------- 
    fold=listdir(pathNameLabels_exo)
    for path_folder in fold:
        # ------------données train exogénes--------------------
        if 'train' in path_folder :
            with open(pathNameLabels_exo+'/'+path_folder) as f:
                vect=np.zeros(3)
                line=f.readline()
                l=0
                i=0
                while line:
                    #recuperer que les 3 dernieres lignes (données exogénes)
                    l+=1
                    if l>5:
                        vect[i]=(int(line))
                        i+=1
                        line=f.readline()
                    else:
                        line=f.readline()
                        
            y_train_exo.append(vect)
        
        #------------données test exogénes---------------------
        if 'test' in path_folder :
            with open(pathNameLabels_exo+'/'+path_folder) as f:
                vect=np.zeros(3)
                line=f.readline()
                l,i=0,0
                while line:
                    #recuperer que les 3 dernieres lignes (données exogénes)
                    l+=1
                    if l>5:
                        vect[i]=(int(line))
                        i+=1
                        line=f.readline()
                    else:
                        line=f.readline()
        
            y_test_exo.append(vect)
            
        
    
#------------------------------------Image------------------------------------------------   
    for img in glob.glob(pathNameImg):   
        if 'train' in img : 
            n= np.array(mpimg.imread(img))
            x_train.append(n)
        if 'test' in img :
            n= mpimg.imread(img)
            x_test.append(n)
    y_train_exo=np.array(y_train_exo)
    y_test_exo=np.array(y_test_exo)
    x_train=np.array(x_train)
    x_test=np.array(x_test)
    return x_train,x_test,y_train, y_test,y_train_exo,y_test_exo