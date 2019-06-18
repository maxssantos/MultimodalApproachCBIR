import numpy as np
import sys
import matplotlib.pyplot as plt
import imageio as im
import collections as cl
import tqdm as tq

sys.path.append('../extractor')
import feature_extractor_bib as feb

def load_parameters():
    k = int(input())
    query_img = str(input()).rstrip()
    imgs_total = int(input())
    dist_f = str(input()).rstrip()
    descs_total = int(input())
    
    desc_files = []
    for i in range(descs_total):
        desc_files.append(str(input()).rstrip())

    return k, query_img, imgs_total, dist_f, desc_files


def load_concatenated_descriptors(desc_files, imgs_total):

    #opening each descriptor file
    descs_total = len(desc_files)
    files = []
    for i in range(descs_total):
        files.append(open(desc_files[i]))

    #loading dataset description that contains the name of each image
    # and the feature vectors of each image and concatenating him
    D = {}
    print("Loading features from dataset")
    for i in tq.tqdm(range(imgs_total)):
        aux = ''
        for j in range(1,descs_total):
            aux += files[j].readline()[0:-1] + ','
        
        #adding new feature vector to list
        D[str(files[0].readline()[0:-1])] = list(map(int, aux[0:-1].split(',')))
        
    #closing each descriptor file
    for i in range(descs_total):
        files[i].close()
    
    return D

#recovering the concatenated descriptors of query image
def query_img_desc(QImg, DFiles):
    H = []
    print("Extracting features from query image")
    for i in tq.tqdm(range(1, len(DFiles))):
        desc = DFiles[i].split('/')[-1].split('.')[0]
        img = im.imread(QImg)
        if desc == 'BIC':
            H += feb.BIC(img, 64)
        elif desc == 'LBP':
            H += feb.LPB(img)
    
    return np.asarray(H).astype(np.float64)

def euclidean_dist(A, B):
    return np.sum( (A - B)**2 ) ** 0.5

def distance(A, B, type):
    if (type == 'euclidean'):
        return euclidean_dist(A, B)

def toClass(ImgPath):
    a = str(ImgPath.split('/')[-1])
    b = a.split('_')
    c = str(b[-1]).split('.')[0]
    d = [b[1], c]
    #d = [b[0], b[1], c]
    tClass = '_'.join(d)
    return tClass

#start############################################################################
# Main Function responsible for:
# 1) load input parameters
# 2) execute KNN
# 3) return the k similar images from query image
# 4) calc the precision and revocation metric 

def main():

    k, ImgQ_path, imgs_total, F, DFiles  = load_parameters()

    V = load_concatenated_descriptors(DFiles, imgs_total)

    QImg = query_img_desc(ImgQ_path, DFiles)

    d = {}

    res = {}

    H = {}

    print("Calculating euclidean distance between query image and other images")
    for ind, val in tq.tqdm(V.items()):
        d[ind] = distance(QImg, val, F)

    res = sorted(d.items(), key=lambda t: t[1])[1:k+1]
    
    img = im.imread(ImgQ_path)
    plt.figure(figsize=(2*k,2*k))
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.subplot(k+1, 1, 1)
    plt.axis('off')
    plt.title('Query Image: '+ toClass(ImgQ_path))
    plt.imshow(img, cmap='gray')

    i = 1
    imgs_path = '/'.join(ImgQ_path.split('/')[0:-1]) + '/'
    for ind, val in res:
        imgname = imgs_path+str(ind)+'.jpg'
        classImg = str(toClass(imgname))
        img = im.imread(imgname)
        plt.subplot(k+1, 1, i+1)        
        plt.axis('off')
        plt.title(str(i)+'ª Similar Image: '+ classImg)
        plt.imshow(img, cmap='gray')

        if (H.get(classImg) == None):
            H[classImg] = 1
        else:
            H[classImg] += 1

        i += 1

    classPredict = sorted(H.items(), key=lambda t: t[1])[-1]
    print("Class: " + str(classPredict[0]))
    print("Precision: " + str(classPredict[1] / k))
    
    plt.show()


#end##############################################################################

# Execution of Program
main()