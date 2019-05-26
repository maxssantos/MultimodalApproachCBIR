# A Multimodal Approach in Content Based Image Retrieval

SCC5830: Digital Image Processing

Maxwell Sampaio dos Santos NUSP: 11186454


## Abstract
Retrieving similar images from large databases is a complex task for the human being. The purpose of this work is to use one technique for extracting and combining the image descriptors (texture, color and/or shape) to enrich content-based image retrieval in the context of medical images. To analyze the proposed technique, the MINI-MIAS dataset was chosen, composed by 118 valid ROIs of mixed mammogram views. Given a query image will be calculated the accuracy and recall of the content-based image retrieving, as a form of evaluation of the proposed technique. All this work will be implemented in the Python language.


## Description of Input Images
The chosen dataset, to apply the proposed technique, was MINI-MIAS (Mammographic Image Analysis Society) dataset and it's available online. This data set consists of 322 images with a resolution of 1024 x 1024 pixels. The list is arranged in pairs of imagens, where each pair represents the left (even filename numbers) and right mammograms (odd filename numbers) of a single patient. 

In addition to the images, MINI-MIAS provides metadata corresponding to the background tissue, class and severity of the abnormality, as well as coordinates to the center of the abnormality and the approximate radius of a circle enclosing it. Such coordinates and radius allowed us to extract the ROIs from the images, which is important in pre-processing as a segmeation step of original images set.

¹: The MINI-MIAS repository: http://peipa.essex.ac.uk/info/mias.html

The properties of gravity (malignant and benign) and class (Calcification (CALC), Well-defined/circumscribed masses (CIRC), Spiculated masses (SPIC), Other ill-defined masses (MISC), Architectural distortion (ARCH), Asymmetry (ASYM), Normal (NORM)) of the abnormality, present in each one of the images, will be important to indicate if, given a query image, the most similar k-images returned by the proposed program belong to the same class and gravity of the query image.

In figure below, examples of images belonging to each of the classes are displayed: (a) CALC, (b) CIRC, (c) SPIC, (d) MISC, (e) ARCH, (f) ASYM and (g) NORM

![CALC Image](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/MIAS-Class-Images-Examples.png "MIAS Class Image Examples")


## Steps
The following steps are proposed to achieve the goal:

### 1. Segmetation of ROIs
In this step, the original images will be segmented into ROIs, according to the coordinates (x,y position and radius size) present in each image of the MINI-MIAS dataset.

### 2. Image Descriptors Extraction
An image descriptor (color, texture or shape) is composed of (i) characteristics vector and (ii) distance function. In this work, will be implemented and used the Border/Interior Classification (BIC) as color's descriptor of the image, and the Local binary patterns (LBP) as texture's descriptor of the image.

### 3. Descriptors Combination
The combination of the descriptors will be performed with the concatenation between the color and texture vectors of a given image, which will make it possible to use a distance / similarity function, for example Euclidean, between any two images.

### 4. Recovery of K Similar Images
In this step, given a query image (Img) and an integer value (K). The program will return the K images most similar to Img, using the K-Nearest Neighbors (KNN) algorithm.

### 5. Accuracy and Recall Calculation
In this final step, the program will calculate the precision (number of correct positive results divided by the number of all positive results returned by the classifier) and the recall (number of correct positive results divided by the number of all relevant samples, ie, all samples that should have been identified as positive).


## Program
There are three programs:
1. [code/segmentation/roi_segmentation.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/segmentation/roi_segmentation.py "ROI Segmentation"): responsible for segmenting the images in Regions of Interest (ROI), according to the coordinates present in each image.
2. [code/extractor/feature_extractor.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/extractor/feature_extractor.py "Feature Extractor"):  responsible for extracting the descriptors (color and texture) of the images set.
3. [code/cbir/cbir.py](https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/cbir/cbir.py "Mammographics CBIR"): responsible for (i) combining the feature vectors (color and shape), (ii) calculating the distances between the query image for all other images and (iii) returning the most similar images to the query image.

The file [code/extractor/feature_extractor_bib.py] (https://github.com/maxssantos/MultimodalApproachCBIR/blob/master/code/extractor/feature_extractor_bib.py "Feature Extractor"): contains a set of functions (created by the author) that are important and necessary for extracting the images descriptors. This file is imported by both files described previously.

## References
[1] Suckling, J., Parker, P., Dance, D. R., Astley, S., Hutt, I., Boggis, C., and Ricketts, I.
(1994). The mammographic image analysis society digital mammogram database.
Excerpta Medica, 1069:375–378.
