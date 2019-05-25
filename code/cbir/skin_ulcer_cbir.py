import numpy as np
import sys
sys.path.append('../extractor')
import feature_extractor_bib as feb
import matplotlib.pyplot as plt
import imageio as im

def load_parameters():
    k = int(input())
    query_img = str(input()).rstrip()
    imgs_total = int(input())
    dist_f = str(input()).rstrip()
    sim_l = float(input())
    descs_total = int(input())
    
    desc_files = []
    for i in range(descs_total):
        desc_files.append(str(input()).rstrip())

    return k, query_img, imgs_total, dist_f, sim_l, desc_files


def load_concatenated_descriptors(desc_files, imgs_total):

    #opening each descriptor file
    descs_total = len(desc_files)    
    files = []
    for i in range(descs_total):
        files.append(open(desc_files[i]))

    #loading the feature vectors of each image and concatenating him
    L = []
    for i in range(imgs_total):
        aux = ''
        for j in range(descs_total):
            aux += files[j].readline()[0:-1] + ','
        
        #removing ',' from the end string
        aux = aux[0:-1]

        #adding new feature vector to list
        L.append(list(map(int, aux.split(','))))
    
    #closing each descriptor file
    for i in range(descs_total):
        files[i].close()
    
    return np.asarray(L)


def query_img_desc(QImg, DFiles):
    H = []
    for i in range(len(DFiles)):
        desc = DFiles[i].split('/')[-1].split('.')[0]
        if desc == 'BIC':
            H += feb.BIC(QImg).tolist()
        elif desc == 'LBP':
            H += feb.LPB(QImg).tolist()
    
    return np.asarray(H)

def euclidean_dist(A, B):
    return np.sum((A - B)**2)**0.5

def distance(A, B, type):    
    if (type == 'euclidean'):
        return euclidean_dist(A, B)

def last_index(s,c):
    i = s.index(c)
    j = i
    print(s, j)
    while(i >= 0):
        j = i
        t = s[j+1:]        
        i = t.index(c)
        print(t, i)

#start############################################################################
# Main Function responsible for:
# 1) load input parameters
# 2) execute KNN
# 3) return the k similar images from query image
# 4) calc the precision and revocation metric 

def main():

    k, QImg_path, imgs_total, Func, lim, DFiles  = load_parameters()

    V = load_concatenated_descriptors(DFiles, imgs_total)

    QImg = query_img_desc(QImg_path, DFiles)

    imgs_path = '/'.join(QImg_path.split('/')[0:-1]) + '/'

    d = {}

    res = []

    for i in range(imgs_total):
        d[i] = distance(QImg, V[i], Func)

    sorted_d = sorted(d.items(), key=lambda t: t[1])
    
    #print(sorted_d)
    x = 0
    for i,v in sorted_d:
        x += 1
        if x <= k:
            res.append(i)
        else:
            break

    img = im.imread(QImg_path)
    plt.figure(figsize=(15,10))
    plt.subplot(2, k, ((k+1)//2))
    plt.axis('off')
    plt.title('Query Image')
    plt.imshow(img)

    i = 1
    img = []
    for x in res:
        img = im.imread(imgs_path+str(x)+'.jpg')
        plt.subplot(2, k, i+k)
        plt.axis('off')
        plt.title(str(i)+'ª Similar Image')
        plt.imshow(img)
        i += 1
    plt.show()

#end##############################################################################

# Execution of Program
main()