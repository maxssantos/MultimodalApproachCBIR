import os
import sys
import numpy as np
import collections as cl
import imageio as im
import tqdm as tq

#start############################################################################
# Function responsible for calculate the color feature vector of image I
def BIC(I, factor):
    HI = list(0 for _ in range (factor)) #histogram for interior pixels quantized in number of factor gray levels
    HE = list(0 for _ in range (factor)) #histogram for exterior pixels quantized in number of factor gray levels
    N, M = I.shape
    
    for x in range(N):
        for y in range(M):
            ind = int((I[x][y] / 255) * (factor-1))

            #pixels from image edge are exterior pixels
            if (x == 0 or y ==0 or x+1 == N or y+1 == M):
                HE[ind] += 1
            #others pixels
            else:
                #pixel [x][y] is equal to its 4-neighbors so it's interior pixel otherwise it's exterior pixel
                if (I[x][y] == I[x][y-1] and I[x][y] == I[x][y+1] and I[x][y] == I[x-1][y] and I[x][y] == I[x+1][y] ):
                    HI[ind] += 1
                else:
                    HE[ind] += 1
    return HI + HE

#end##############################################################################

#start############################################################################
# Function responsible for calculate the texture feature vector of image I
def LPB(I):    

    #start############################################################################
    def extractor(R,F):
        E = np.zeros(R.shape, dtype=np.uint8)
        E[ np.where(R >= R[1][1]) ] = 1
        E[1][1] = 0
        return np.sum(E*F)
    #end##############################################################################


    #start def LPB(I):################################################################
    H = list(0 for _ in range (256)) # histogram result for LBP
    N, M = I.shape

    #LBP 3x3 weights matrix
    F = np.array([[8, 4, 2], [16, 0, 1], [32, 64, 128]], dtype=np.uint8)

    for x in range(1,N-1):
        for y in range(1,M-1):
            H[extractor(I[x-1:x+2, y-1:y+2], F)] += 1
    return H

#end##############################################################################

#start############################################################################
# Function responsible for (1) identifing the type of color and texture descriptor,
# (2) calculating the corresponding feature vectors and (3) creating CSV file for 
# each feature type
def fe(d_in, d_out, d_color='BIC', d_text='LBP', total_images=0):    
    for imgName in tq.tqdm(sorted(os.listdir(d_in))):
        arq1 = open(d_out+'description.csv', 'a')
        arq2 = open(d_out+d_color+'.csv', 'a')
        arq3 = open(d_out+d_text+'.csv', 'a')
    
        ind = imgName.split('.')[0]
        img = im.imread(d_in+imgName)

        if d_color == 'BIC':
            C = BIC(img, 64)

        if d_text == 'LBP':
            T = LPB(img)
        
        arq1.write(str(ind)+"\n")
        arq2.write(",".join(str(x) for x in C) + '\n')
        arq3.write(",".join(str(x) for x in T) + '\n')
        
        arq1.close()
        arq2.close()
        arq3.close()
#end##############################################################################