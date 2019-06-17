from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

import matplotlib.pyplot as plt

def create_dataset(desc_files, imgs_total):
    #opening each descriptor file
    descs_total = len(desc_files)
    files = []
    for i in range(descs_total):
        files.append(open(desc_files[i]))

    #loading dataset description that contains the name of each image
    # and the feature vectors of each image and concatenating him
    D = {}
    C = {}
    L = {}
    N = {}
    l = 0
    for i in range(imgs_total):
        aux = ''
        for j in range(1,descs_total):
            aux += files[j].readline()[0:-1] + ','
        
        #adding new feature vector to the list
        D[i] = list(map(int, aux[0:-1].split(',')))
        
        #Image Name
        N[i] = str(files[0].readline()[0:-1])
        
        a = N[i].split('_')
        b = [a[1], a[4]]
        label = '_'.join(b)

        if (C.get(label) == None):
            C[label] = l
            l += 1

        L[i] = C[label]
        
    #closing each descriptor file
    for i in range(descs_total):
        files[i].close()
    
    return D, L, N, C

def load_parameters():
    Ks = list(map(int, str(input()).rstrip().split(' ')))
    imgs_total = int(input())
    dist_f = str(input()).rstrip()
    descs_total = int(input())
    
    desc_files = []
    for _ in range(descs_total):
        desc_files.append(str(input()).rstrip())

    return Ks, imgs_total, dist_f, desc_files

#start############################################################################
# Main Function responsible for:
# 1) load input parameters
# 2) execute KNN Classifier

def main():

    #K: vector k initial and final, M: total amount images, F: distance function, DFiles: list of CSV Files
    K, M, F, DFiles  = load_parameters()

    #D: dataset, L: class, N: Name, C: classNames
    D, L, N, C = create_dataset(DFiles, M)
    
    #separating dataset at 30% for test and 70% for training
    x_train, x_test, y_train, y_test = train_test_split(D, L, test_size = 0.30, random_state=4)

    #calculating and ploting the accuracy for each value of k in the range
    #using KNN as classifier
    k_range = range(K[0], K[1]+1)
    hits = {}
    hits_list = []
    best_accuracy = 0
    best_k = 0
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k, metric=F)
        knn.fit(x_train, y_train)
        y_pred = knn.predict(x_test)
        accuracy = metrics.accuracy_score(y_test, y_pred)
        if (accuracy > best_accuracy):
            best_accuracy = accuracy
            best_k = k
        hits_list.append(accuracy)
    

    # knn = KNeighborsClassifier(n_neighbors=best_k, metric=F)
    # knn.fit(x_train, y_train)
    # y_pred = knn.predict(x_test)

    plt.plot(k_range, hits_list)
    plt.xlabel('Value of K for KNN')
    plt.ylabel('Test Accuracy')
    plt.show()
#end##############################################################################

# Execution of Program

#parameters
#1º: variation of the value of k (1 20, for example)
#2º: total amount of images
#3º: distance function name (euclidean, manhattan, chebyshev, minkowski, wminkowski, seuclidean, mahalanobis)
#3º: number of feature types, counting the first characteristic as the class that each image belongs to
#4º: CSV file containing the class of each image
#5º to nº: CSV files containing a certain characteristic (LBP or BIC) extracted from the images   

main()