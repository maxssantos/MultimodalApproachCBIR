from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

import matplotlib.pyplot as plt
import tqdm as tq
import random as rd
import sys

def create_dataset(desc_files, imgs_total, qipath):
    #opening each descriptor file
    descs_total = len(desc_files)
    files = []
    for i in range(descs_total):
        files.append(open(desc_files[i]))

    #loading dataset description that contains the name of each image
    # and the feature vectors of each image and concatenating him
    D = {} #dataset
    C = {} #mapping image class
    L = {} #dataset class
    N = {} #image names

    QI = [] #query image
    QIC = [] #query image class

    qiname = str(qipath.split('/')[-1])

    r = 0
    print("Loading features from dataset")
    i = 0
    for _ in tq.tqdm(range(imgs_total)):
        aux = ''
        for j in range(1,descs_total):
            aux += files[j].readline()[0:-1] + ','

        vec = list(map(int, aux[0:-1].split(',')))
        cname = str(files[0].readline()[0:-1]) 
        
        a = cname.split('_')
        b = [a[1], a[4]]
        label = '_'.join(b)

        if (C.get(label) == None):
            C[label] = r
            r += 1

        if (cname != qiname):
            
            #adding new feature vector to the list
            D.update({i : vec})
            
            #Image Name
            N.update({i : cname})

            #image class
            L.update({i : C[label]})

            i+=1
        else:
            QI.append(vec)
            QIC.append(C[label])
        
    #closing each descriptor file
    for i in range(descs_total):
        files[i].close()
    
    return D, L, N, C, QI, QIC

def load_parameters():
    Ks = list(map(int, str(input()).rstrip().split(' ')))
    imgs_total = int(input())    
    qipath = str(input()).rstrip()
    dist_f = str(input()).rstrip()
    descs_total = int(input())
    
    desc_files = []
    for _ in range(descs_total):
        desc_files.append(str(input()).rstrip())

    return Ks, imgs_total, dist_f, desc_files, qipath

#start############################################################################
# Main Function responsible for:
# 1) load input parameters
# 2) made the KNN Classifier Template
# 3) testing template for obtain the best K
# 4) 

def main():

    #K: vector k initial and final, M: total amount images, F: distance function, DFiles: list of CSV Files
    K, M, F, DFiles, qipath  = load_parameters()

    #D: dataset, L: class, N: Name, C: classNames
    D, L, N, C, QI, QIC = create_dataset(DFiles, M, qipath)

    #separating dataset at 30% for test and 70% for training with seed random egual to 4
    x_train, x_test, y_train, y_test = train_test_split(D, L, test_size = 0.30, random_state=4)
    
    if (len(K) == 2):

        #calculating the accuracy for each value of k in the range
        #using KNN as classifier for to find the best k
        k_range = range(K[0], K[1]+1)
        hits_list = []
        best_accuracy = 0
        best_k = 0
        print("Testing variation of K")
        for k in tq.tqdm(k_range):
            knn = KNeighborsClassifier(n_neighbors=k, metric=F)
            knn.fit(x_train, y_train)
            y_pred = knn.predict(x_test)
            accuracy = metrics.accuracy_score(y_test, y_pred)
            if (accuracy > best_accuracy):
                best_accuracy = accuracy
                best_k = k
            hits_list.append(accuracy)

        print("Best K: "+ str(best_k))
        print("Best Precision: "+ str(best_accuracy))

        plt.plot(k_range, hits_list)
        plt.xlabel('Value of K for KNN')
        plt.ylabel('Test Accuracy')
        plt.show()
    else:
        best_k = K[0]
    
    #Classifing the query image using the best k
    knn = KNeighborsClassifier(n_neighbors=best_k, metric=F)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    model_accuracy = metrics.accuracy_score(y_test, y_pred)
    
    y_pred = knn.predict(QI)
    accuracy = metrics.accuracy_score(QIC, y_pred)

    print("Classifier Model Precision: " + str(model_accuracy))
    print("Query Image: " + qipath)
    print("Query Image Class Predict: " + str(y_pred [0]) + '=>' + str(list(C.keys())[y_pred [0] ] ) )
    print("Query Image Precision: " + str(accuracy))

#end##############################################################################

# Execution of Program

#parameters
#1º: variation of the value of k (1 20, for example)
#2º: total amount of images
#3º: distance function name (euclidean, manhattan, chebyshev, minkowski)
#3º: number of feature types, counting the first characteristic as the class that each image belongs to
#4º: CSV file containing the class of each image
#5º to nº: CSV files containing a certain characteristic (LBP or BIC) extracted from the images   

main()