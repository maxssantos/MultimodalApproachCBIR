# A Multimodal Approach in Content Based Image Retrieval

SCC5830: Digital Image Processing

Maxwell Sampaio dos Santos NUSP: 11186454


## Abstract
Retrieving similar images from large databases is a complex task for the human being. The purpose of this work is to use one technique for extracting and combining the image descriptors (texture, color and/or shape) to enrich content-based image retrieval in the context of medical images. To analyze the proposed technique, the DDSM dataset was chosen, it's composed of more than three thousand medical breast images. Given a query image will be calculated the accuracy and recall of the content-based image retrieving, as a form of evaluation of the proposed technique. All this work was be implemented in the Python language.


## Description of Input Images
The chosen dataset was DDSM (Digital Dataset for Screening Mammography) [1] and it's available online¹. According to Oliveira et al [2], this dataset consists of more than three thousand medical breast images, organized into 4 (four) categories based on the view of the breast image, which are (i) LCC: Left CranioCaudal, (ii) RCC: Right CranioCaudal, (iii) LMLO: Left MedioLateral Oblique, and (iv) RMLO: Right MedioLateral Oblique. DDSM was originally created in a collaborative effort involving the Massachusetts General Hospital, the University of South Africa and the Sandia National Laboratories. Moreover, additional cases were provided by the Washington University School of Medicine. The current DDSM repository is maintained at University of South Florida. DDSM is divided into cases with annotated labels, which are "malign", or “benign”. At most four images are captured per patient, two on the left side of the chest and two on the right side.

¹: The DDSM repository: [http://marathon.csee.usf.edu/Mammography/Database.html](http://marathon.csee.usf.edu/Mammography/Database.html), also available as a Mammoset subdataset at [https://bitbucket.org/gbdi/mammoset/src](https://bitbucket.org/gbdi/mammoset/src)

The diagnoses (N, C and B) and the classification categories (LCC, RCC, LMLO and RMLO) present in each of the images will be important to indicate if, given a query image, the k images most similar returned by the proposed program belong to the same class of query image.

In figure below, examples of images belonging to each of the classes are displayed: (a) LCC, (b) RCC, (c) LMLO and (d) RMLO

![DDSM Image Examples](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/DDSM_Image_Examples.png "DDSM Image Class Examples")

## Steps
The following steps are proposed to achieve the goal:

### 1. Image Descriptors Extraction
An image descriptor (color, texture or shape) is composed of (i) characteristics vector and (ii) distance function. In this work, was be implemented and used the Border/Interior Classification (BIC) as color's descriptor of the image, and the Local Binary Pattern (LBP) as texture's descriptor of the image. Euclidean was defined as a function of distance in this work. This step spent around 80 hours to extract the two characteristics of each of the 2892 images

### 2. Descriptors Combination
The combination of the descriptors was be performed with the concatenation between the color and texture vectors of a given image, which made it possible to use a distance / likeness function, for example Euclidean, between any two images in the dataset.

### 3. Recovery of K Similar Images
In this step, given a query image (Img) and an integer value (K). The program will return the K images most similar to Img, using the K-Nearest Neighbors (KNN) algorithm, implemented by author.

### 4. Classifier Query Image
It was also created an experiment which used the [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier), available in [sklearn](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors) package Python, to build a program that creates a classifier model. Then an experiment was conducted, iterating k from 1 to 100, to determine the best k value that can optimize the classification accuracy of the constructed model. According to image X the best K was equal to Y. This value of K was then used to reconstruct the classifier model. Lastly, given a query image, the program generates its descriptors (BIC and LBP) and classifies this image, using the template previously created, in one of those 8 classes (4 malign e 4 benign) previously presented.

### 4. Accuracy Calculation
In this final step, the program calculates the precision of the experiments: (i) in the case of step 3 it indicates the precision as the number of similar images belonging to the same class of the query image divided by the total of similar images returned (in this case is k); (ii) in the case of step 4 it indicates the precision based on the construction of the classifier model, where it separates the dataset into training and test.


## Program
It's composed for two programs:
1. [code/extractor/feature_extractor.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/extractor/feature_extractor.py "Feature Extractor"):  responsible for extracting the descriptors (color and texture) of the images set.
2. [code/cbir/cbir.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/cbir/cbir.py "Mammographics CBIR"): it's main program, that is responsible for (i) combining the feature vectors (color and texture), (ii) calculating the distances between the query image for all other images and (iii) returning the most similar k-images to the query image.
3. [code/cbir/knn_classifier.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/cbir/knn_classifier.py "Mammographics CBIR KNN"): this program, that is responsible for (i) creating the classification model using KNeighborsClassifier with 70% of the image set (in the case of LBP and BIC descriptors concatenated) for training and 30% for testing; (ii) given a query image, not belonging to the initial set of images, generate the LBP and BIC descriptors of it and concatenate them; (iii) classify the query image into one of those previously presented classes.


The file [code/extractor/feature_extractor_bib.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/extractor/feature_extractor_bib.py "Feature Extractor"): contains a set of functions (created by the author) that are important and necessary for extracting the images descriptors. This file is imported by last two files described previously.

## References
[1] Heath, M., Bowyer, K., Kopans, D., Moore, R., and Kegelmeyer, W. P. The digital database for screening mammography. In IWDM, pages 212–218. Medical Physics. 2001

[2] Oliveira, P., Scabora, L. C., Cazzolato, M., Bedo, M., Traina, Agma., Jr, Caetano. MAMMOSET: An Enhanced Dataset of Mammograms. Proceedings of the Satellite Events of the 32nd Brazilian Symposium on Databases. 2017
