# A Multimodal Approach in Content Based Image Retrieval

SCC5830: Digital Image Processing

Maxwell Sampaio dos Santos NUSP: 11186454

# Abstract
Retrieving similar images from large databases is a complex task for the human being. The purpose of this work is to use one technique for extracting and combining the image descriptors (texture, color and/or shape) to enrich content-based image retrieval in the context of medical images. To analyze the proposed technique, a proprietary dataset, composed by skin ulcers images, will be used. Given a query image will be calculated the accuracy and recall of the content-based image retrieving, as a form of evaluation of the proposed technique.

# Description of Input Images
The chosen dataset, to apply the proposed technique, is a set of proprietary images provided to the ICMC/USP Data Bases and Images Group (GBDI) by the Clinical Hospital of the Ribeirão Preto Medical School. This dataset is composed of 217 colored dermatological images, with skin ulcers originated from both venous and arterial insufficiencies, and the images were labeled by specialists in the following classes: granulation (G), fibrin (F), callous (C) and necrotic tissue (N).

# Steps
The following steps are proposed to achieve the goal:
1) Image Descriptors Extraction
An image descriptor (color, texture or shape, is composed of a characteristics vector and a similarity function. In this work, will be used to the descriptor  for color and the descriptor for texture.

2) Descriptors Combination
The combination of the descriptors will be performed with the concatenation between the color and texture vectors of a given image and the with the euclidian distance function, aplied as similarity function between two images.

3) Recovery of K Similar Images
In this step, given a query image (Img) and an integer value (K). The program will return the K images most similar to Img, using the K-Means algorithm.

4) Accuracy and Recall Calculation
In this final step, the program will calculate the precision (fraction of recovered images that are relevant) and the recall (fraction of relevant imagens that are retrieved).

