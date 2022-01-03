#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:36:26 2022

@author: master
"""

def visualise(history):
    """
    fonction qui permet de visualiser l'historique du modele
    """

    fig,axs = plt.subplots(2) 
    # create accuracy sublpot 
    axs[0].plot(history.history["accuracy"], label="train accuracy") 
    axs[0].set_ylabel("Accuracy") 
    axs[0].legend(loc="lower right") 
    axs[0].set_title("Accuracy eval")

    # create error sublpot 
    axs[1].plot(history.history["loss"], label="train error") 
    axs[1].set_ylabel("Error") 
    axs[1].set_xlabel("Epoch") 
    axs[1].legend(loc="upper right") 
    axs[1].set_title("Error eval") 

    plt.show()
