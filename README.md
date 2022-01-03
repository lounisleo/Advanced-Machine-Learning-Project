# Advanced-Machine-Learning-Project
THIN: THrowable Information Networks and Applicationfor Facial Expression Recognition In The Wild
# M2 ISI - Groupe MLA 16 

Ce dépôt contient les éléments de base de notre projet de l'implimentation du model THIN pour reconnaisance d'expressions faciales.

# :wave: Contenue 

## 📝 Database 

*Consernant la base de données on a utiliser des images aligned Basic 


## 🤓 Fonctions implimenté 

L'objectif de cette partie est de vous donner une brève explication sur les fonctions implantées et selon quel ordre deverait être appelé. 🚀

##  create_data.py 

Pour déviser les images en train test et les labels endogene et exogenes en train et test.

## data_endo.py 

Permet de de faire un one hot encoding des labele des variables endogene "FER".

## Get_data.py

Permet de recupere nos donner "les images du visage "et leurs label "exogene/ endogene "

##  shape_data_exo.py

Permet de de faire un one hot encoding des labele des variables exogene "Le genre", "La race", " L'age" .

##  visualise.py

Cette fonction permet de tracer l'évolution de la loss et l'accuracy en fonction du nombre d'epochs.

##  train_model_exogenous.py

Cette fonction permet d'entrainer les modeles exagenous representation définit avec keras pour "Le genre", "La race", " L'age". 

## Prediction_GRA 

Cette fonction permet predire le variables exogenes  "Le genre", "La race", " L'age" .

## Deep_ensemble 

Contient le classifieur deep ensemble 

## endo_exo_representation.py

Défint les 2 modeles exogene et endogene representation à l'aide de keras

## Exagenous_classifier.py

Définit l'autoencodeur Exagenous classifier

## Tree_gate.py 

Définit le bloc Deep Tree Gate 

##  
## 💻 Notebook  : THIN_code

Un notebook est présent pour faire la démonstration des différentes fonctions. 
