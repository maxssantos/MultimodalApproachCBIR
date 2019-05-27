# A Multimodal Approach in Content Based Image Retrieval

SCC5830: Digital Image Processing

Maxwell Sampaio dos Santos NUSP: 11186454


## Abstract
Retrieving similar images from large databases is a complex task for the human being. The purpose of this work is to use one technique for extracting and combining the image descriptors (texture, color and/or shape) to enrich content-based image retrieval in the context of medical images. To analyze the proposed technique, the DDSM dataset was chosen, it's composed of more than three thousand medical breast images. Given a query image will be calculated the accuracy and recall of the content-based image retrieving, as a form of evaluation of the proposed technique. All this work will be implemented in the Python language.


## Description of Input Images
The chosen dataset was DDSM (Digital Dataset for Screening Mammography) [1] and it's available online¹. According to Oliveira et al [2], this dataset consists of more than three thousand medical breast images, organized into 4 (four) categories based on the view of the breast image, which are (i) LCC: Left CranioCaudal, (ii) RCC: Right CranioCaudal, (iii) LMLO: Left MedioLateral Oblique, and (iv) RMLO: Right MedioLateral Oblique. DDSM was originally created in a collaborative effort involving the Massachusetts General Hospital, the University of South Africa and the Sandia National Laboratories. Moreover, additional cases were provided by the Washington University School of Medicine. The current DDSM repository is maintained at University of South Florida. DDSM is divided into cases with annotated labels, which are “normal”, “cancer”, or “benign”. In the maximum of four images is assigned to one patient, two for the left breast and two for the right breast.

¹: The DDSM repository: [http://marathon.csee.usf.edu/Mammography/Database.html](http://marathon.csee.usf.edu/Mammography/Database.html), also available as a Mammoset subdataset at [https://bitbucket.org/gbdi/mammoset/src](https://bitbucket.org/gbdi/mammoset/src)

The diagnoses (N, C and B) and the classification categories (LCC, RCC, LMLO and RMLO) present in each of the images will be important to indicate if, given a query image, the most similar k images returned by the proposed program belong to the same class and the image of the query.

In figure below, examples of images belonging to each of the classes are displayed: (a) LCC, (b) RCC, (c) LMLO and (d) RMLO

![DDSM Image Examples](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/DDSM_Image_Examples.png "DDSM Image Class Examples")

## Steps
The following steps are proposed to achieve the goal:

### 1. Image Descriptors Extraction
An image descriptor (color, texture or shape) is composed of (i) characteristics vector and (ii) distance function. In this work, will be implemented and used the Border/Interior Classification (BIC) as color's descriptor of the image, and the Local binary patterns (LBP) as texture's descriptor of the image.

### 2. Descriptors Combination
The combination of the descriptors will be performed with the concatenation between the color and texture vectors of a given image, which will make it possible to use a distance/similarity function, for example Euclidean, between any two images.

### 3. Recovery of K Similar Images
In this step, given a query image (Img) and an integer value (K). The program will return the K images most similar to Img, using the K-Nearest Neighbors (KNN) algorithm.

### 4. Accuracy and Recall Calculation
In this final step, the program will calculate the precision (number of correct positive results divided by the number of all positive results returned by the classifier) and the recall (number of correct positive results divided by the number of all relevant samples, ie, all samples that should have been identified as positive).


## Program
It's composed for two programs:
1. [code/extractor/feature_extractor.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/extractor/feature_extractor.py "Feature Extractor"):  responsible for extracting the descriptors (color and texture) of the images set.
2. [code/cbir/cbir.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/cbir/cbir.py "Mammographics CBIR"): it's main program, that is responsible for (i) combining the feature vectors (color and texture), (ii) calculating the distances between the query image for all other images and (iii) returning the most similar k-images to the query image.

The file [code/extractor/feature_extractor_bib.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/extractor/feature_extractor_bib.py "Feature Extractor"): contains a set of functions (created by the author) that are important and necessary for extracting the images descriptors. This file is imported by last two files described previously.

## References
[1] Heath, M., Bowyer, K., Kopans, D., Moore, R., and Kegelmeyer, W. P. (2001). The digital
database for screening mammography. In IWDM, pages 212–218. Medical Physics.
[2] Oliveira, Paulo & de Carvalho Scabora, Lucas & Cazzolato, Mirela & Bedo, Marcos & Traina, Agma & Jr, Caetano. (2017). MAMMOSET: An Enhanced Dataset of Mammograms. Proceedings of the Satellite Events of the 32nd Brazilian Symposium on Databases.
