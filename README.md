# A Multimodal Approach in Content Based Image Retrieval

SCC5830: Digital Image Processing

Maxwell Sampaio dos Santos NUSP: 11186454


## Abstract
Retrieving similar images from large databases is a complex task for the human being. The purpose of this work is to use one technique for extracting and combining the image descriptors (texture, color and/or shape) to enrich content-based image retrieval in the context of medical images. To analyze the proposed technique, the DDSM dataset was chosen, it's composed of more than three thousand medical breast images. Given a query image will be calculated the accuracy of the content-based image retrieving, as a form of evaluation of the proposed technique. All this work was be implemented in the Python language.


## Description of Input Images
The chosen dataset was DDSM (Digital Dataset for Screening Mammography) [1] and it's available online¹. According to Oliveira et al [2], this dataset consists of almost than three thousand medical breast images, organized into 4 (four) categories based on the view of the breast image, which are (i) LCC: Left CranioCaudal, (ii) RCC: Right CranioCaudal, (iii) LMLO: Left MedioLateral Oblique, and (iv) RMLO: Right MedioLateral Oblique. The CranioCaudal (CC) view which is a top-bottom view of the breast and the MedioLateral Oblique (MLO) view which is a side view of the breast taken at a certain angle. DDSM was originally created in a collaborative effort involving the Massachusetts General Hospital, the University of South Africa and the Sandia National Laboratories. Moreover, additional cases were provided by the Washington University School of Medicine. The current DDSM repository is maintained at University of South Florida. DDSM is divided into cases with annotated labels, which are "malign", or “benign”. At most four images are captured per patient, two on the left side of the chest and two on the right side. All images are Region of Interest (ROI) with 1000 x 1000 pixels, filled with zeros, in cases of ROIs with smaller dimensions.

¹: The DDSM repository: [http://marathon.csee.usf.edu/Mammography/Database.html](http://marathon.csee.usf.edu/Mammography/Database.html), also available as a Mammoset subdataset at [https://bitbucket.org/gbdi/mammoset/src](https://bitbucket.org/gbdi/mammoset/src)

The diagnoses (Malign-M and Benign-B) and the classification categories (LCC, RCC, LMLO and RMLO) present in each of the images wa be important to indicate if, given a query image, the k images most similar returned by the proposed program belong to the same class of query image.

In Figure 1 below, examples of images belonging to each of the classes are displayed: (a) LCC, (b) RCC, (c) LMLO and (d) RMLO

![DDSM Image Examples](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/DDSM_Image_Examples.png "DDSM Image Class Examples")

## Steps
The following steps are proposed to achieve the goal:

### 1. Image Descriptors Extraction
An image descriptor (color, texture or shape) is composed of (i) characteristics vector and (ii) distance function. In this work, was be implemented and used the Border/Interior Classification (BIC)[3] as color's descriptor of the image, and the Local Binary Pattern (LBP)[4] as texture's descriptor of the image. Euclidean was defined as a function of distance in this work. This step spent around 80 hours to extract the two features of each of the 2892 images

### 2. Descriptors Combination
The combination of the descriptors was be performed with the concatenation between the color and texture vectors of a given image, which made it possible to use a distance / likeness function, for example Euclidean, between any two images in the dataset.

### 3. Recovery of K Similar Images
In this step, given a query image (Img) and an integer value (K). The program will return the K images most similar to Img, using the K-Nearest Neighbors (KNN) algorithm, implemented by author.

### 4. Classifier Query Image
It was also created an experiment which used the [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier), available in [sklearn](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors) package Python, to build a program that creates a classifier model. Then an experiment was conducted, iterating k from 1 to 100, to determine the best k value that can optimize the classification accuracy of the constructed model. According to Figure 2 the best K was equal to 5.

![The_Best_K](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/Figure_2.png "The Best K of KNN Classifier")

This value of K was then used to reconstruct the classifier model. Lastly, given a query image, the program generates its descriptors (BIC and LBP) and classifies this image, using the template previously created, in one of those 8 classes (4 malign e 4 benign) previously presented. As a final result we obtained a prediction of about 19% in the built-in classifier model, which is low, and this reflected in the misclassification of the query image, which he accused of being of class RMLO_B being that the image is of class RMLO_M.

### 5. Accuracy Calculation
In this final step, the program calculates the precision of the experiments: (i) in the case of step 3, it indicates the precision as the number of similar images belonging to the same class of the query image divided by the total of similar images returned (in this case is k); (ii) in the case of step 4 it indicates the precision based on the construction of the classifier model, where it separates the dataset into training and test.


## Program
It's composed for two programs:
1. [code/extractor/feature_extractor.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/extractor/feature_extractor.py "Feature Extractor"):  responsible for extracting the descriptors (color and texture) of the images set.
2. [code/cbir/cbir.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/cbir/cbir.py "Mammographics CBIR"): it's main program, that is responsible for (i) combining the feature vectors (color and texture), (ii) calculating the distances between the query image for all other images and (iii) returning the most similar k-images to the query image.
3. [code/cbir/knn_classifier.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/cbir/knn_classifier.py "Mammographics CBIR KNN"): this program, that is responsible for (i) creating the classification model using KNeighborsClassifier with 70% of the image set (in the case of LBP and BIC descriptors concatenated) for training and 30% for testing; (ii) given a query image, not belonging to the initial set of images, generate the LBP and BIC descriptors of it and concatenate them; (iii) classify the query image into one of those previously presented classes.

The file [code/extractor/feature_extractor_bib.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/extractor/feature_extractor_bib.py "Feature Extractor Bib"): contains a set of functions (created by the author) that are important and necessary for extracting the images descriptors. This file is imported by last two files described previously.

## Experiments
Before performing the experiments it was necessary to extract the BIC and LBP descriptors from each of the 2892 dataset images. Using algorithms, implemented by the author in the [code/extractor/feature_extractor.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/extractor/feature_extractor.py "Feature Extractor") and [feature_extractor_bib.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/extractor/feature_extractor_bib.py "Feature Extractor Bib") files, a CSV file was generated for each descriptor type, the [descriptors/DDSM/BIC.csv](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/descriptors/DDSM/BIC.csv) file, and the [descriptors/DDSM/LPB.csv](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/descriptors/DDSM/LBP.csv) file. Each line of the CSV file, in the case of the first file, contains a sequence of 128 comma-separated integers where the first 64 numbers represent the histogram of the inner pixels and the other 64 represent the histogram of the outer pixels. The second CSV file contains a sequence of 256 integers representing the histogram of the local binary pattern found in each of the images. This entire extraction process took about 84 hours to complete, using an Intel (R) Core i7 2.67GHz computer, 8GB of RAM and Ubuntu 18.04 64bit.

The first experiment, according to the input file [code/cbir/1.in](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/cbir/1.in), was to perform the prediction of the class of the query image, randomly chosen, "usf0008_RMLO_L1_MS_M" through the KNN, implemented by the author in the file [code/cbir/cbir.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/cbir/cbir.py). It used a value of k equal to 10, Euclidean distance function and concatenation of the BIC and LBP descriptors, exactly in this sequence, on the set of 2892 images. As a result, the query image erroneously classified as belonging to the class "RMLO_B", it belongs to class "RMLO_M", with 33% accuracy, that is, of the 10 most similar images returned, 3 of them belong to the class "RMLO_B", and therefore the class of the query image should be this, but it was not.

The second experiment, according to input file [code/cbir/2.in](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/cbir/2.in), consisted in realizing the discovery of what would be the best value of k to be used in the KNN and then classifying the image "usf0008_RMLO_L1_MS_M". In this experiment, using the [sklearn](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors) package implemented in the file [code/cbir/knn_classifier.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/cbir/knn_classifier.py), it was obtained that the best value of k ranging from 1 to 50, was 5, with accuracy of only 19%, and the dataset of 2982 images was divided into 30 % for test and 70% for training. Then, the query image classification prediction was performed, using k equal to 5 and manhattan distance function, in which once again the query image was erroneously classified as belonging to class "RMLO_B", being that it belongs to the class "RMLO_M"

## Conclusion
As a conclusion of this work it is noticed that the concatenation of the descriptors BIC and LBP (generating a new descriptor) applied to this set of 2982 mammographic images did not obtain satisfactory results and therefore it is important to continue researching other descriptors and/or ways of combining the descriptors to elevate the classification accuracy of the images in this dataset. As well as to test the application of other classification algorithms like those based on rays of similarity coverage and not only in the KNN.

## References
[1] Heath, M., Bowyer, K., Kopans, D., Moore, R., and Kegelmeyer, W. P. The digital database for screening mammography. In IWDM, pages 212–218. Medical Physics. 2001

[2] Oliveira, P., Scabora, L. C., Cazzolato, M., Bedo, M., Traina, Agma., Jr, Caetano. MAMMOSET: An Enhanced Dataset of Mammograms. Proceedings of the Satellite Events of the 32nd Brazilian Symposium on Databases. 2017

[3] Stehling, Renato O., Nascimento, Mario A., Falcão, Alexandre X. A compact and efficient image retrieval approach based on border/interior pixel classification. Proceedings of the Eleventh International Conference on Information and Knowledge Management. McLean, Virginia, USA. ACM. ISBN: 1-58113-492-4. 2002 

[4] Timo Ojala, Matti Pietikäinen, David Harwood. A comparative study of texture measures with classification based on featured distributions. Pattern Recognition, Volume 29, Issue 1, Pages 51-59. ISSN 0031-3203. 1996.
