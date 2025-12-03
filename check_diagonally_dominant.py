import numpy as np

def check_diagonally_dominant(A):
    rows, cols = np.shape(A)
    diagonally_dominant = True
    
    for i in range (rows):

        if(2*abs(A[i,i]) <= sum(abs(A)[i,:])):
            diagonally_dominant = False
    return diagonally_dominant