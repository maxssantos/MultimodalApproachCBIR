import os
import numpy as np
import collections as cl

#start############################################################################
# Function responsible for calculate the color feature vector of image I
def BIC(I):
    return np.random.randint(0,100, [256])

#end##############################################################################

#start############################################################################
# Function responsible for calculate the texture feature vector of image I
def LPB(I):
    return np.random.randint(0,100, [256])

#end##############################################################################

#start############################################################################
# Function responsible for (1) identifing the type of color and texture descriptor,
# (2) calculating the corresponding feature vectors and (3) creating CSV file for 
# each feature type
def fe(d_in, d_out, d_color='BIC', d_text='LBP', total_images=0):
    np.random.seed(666)
    hist_c = cl.OrderedDict()
    hist_t = cl.OrderedDict()
    
    for img in os.listdir(d_in):
        num = int(img.split('.')[0])
        
        if d_color == 'BIC':
            hist_c[num] = BIC(d_in+img)
    
        if d_text == 'LBP':
            hist_t[num] = LPB(d_in+img)

    #saving the texture feature vector in the output directory
    arq = open(d_out+d_color+'.csv', 'w')
    for ind, val in sorted(hist_c.items(), key=lambda t: t[0]):
        arq.write(",".join(str(x) for x in val) + '\n')
    arq.close()

    #saving the texture feature vector in the output directory
    arq = open(d_out+d_text+'.csv', 'w')
    for ind, val in sorted(hist_t.items(), key=lambda q: q[0]):
        arq.write(",".join(str(x) for x in val) + '\n')
    arq.close()
#end##############################################################################