#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:24:24 2022

@author: master
"""

import numpy as np
import glob
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from tensorflow import keras 
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.metrics import multilabel_confusion_matrix
import random
from tensorflow.keras.applications.vgg16 import VGG16 # import pretrained VGG16 model 
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import tensorflow as tf
import shutil
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostClassifier #ensemble methods used 
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score


def create_data():
    """
    fonction pour creer la base de données en faisant appel a la fonction 'PrepareDateSet'
    """
    pwd = '/home/user/data/basic'
    x_train, x_test, y_train_endo, y_test_endo,y_train_exo,y_test_exo=PrepareDateSet(pwd+'/EmoLabel/list_patition_label.txt',pwd+'/Image/aligned/*.jpg',pwd+'/Annotation/manual')

    print('shape de x_train : ',np.shape(x_train))
    print('shape de x_test : ',np.shape(x_test))
    print('shape de y_train_endo : ',np.shape(y_train_endo))
    print('shape de y_test_endo : ',np.shape(y_test_endo))
    print('shape de y_train_exo : ',np.shape(y_train_exo))
    print('shape de y_test_exo : ',np.shape(y_test_exo))
    
    return x_train, x_test, y_train_endo, y_test_endo,y_train_exo,y_test_exo