import matplotlib.pyplot as plt
import numpy as np
from csvManagement import csvToNumpy
from Utilities import suit_np

def plot_init(X,Y):
    fig,ax = plt.subplots(1,2,figsize=(10,5))
    ax[0].scatter(X[:,0],Y,label="Hours Studied")
    ax[1].scatter(X[:,1],Y,label="Attendance")
    ax[0].legend()
    ax[1].legend()
    plt.show()


def plot_final(X,Y,Y_predict):
    fig,ax = plt.subplots(1,3,figsize=(10,5))
    
    tmp_arr = suit_np(100,1)
    ax[0].scatter(X[:,0],Y,label="Hours Studied")
    ax[1].scatter(X[:,1],Y,label="Attendance")
    ax[2].plot(tmp_arr,Y_predict,label="Prediction")
    ax[2].set_xlabel("Hours Studied")
    ax[2].set_ylabel("Attendance")
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()
    plt.show()