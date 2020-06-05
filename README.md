# Predicting-Gene-Regulatory-Interaction-from-Spatial-Data-and-Deep-Learning-Technique

The process of establishing relationship between TF from ISH images can be explained as follows:
(1) Data features extraction from ISH gene expression images. (2) The training labels are comprehended from the previous study
of RNA-Seq data and computation sequence interface.
(3) From the ISH images the image pair is being generated which
serves as the input for the next process.
(4) Convolution Neural Network (CNN) with the ResNet50 model
is used on the data for the prediction system.
(5) The top layer of the REsNet50 model is replaced by Fully
connected layer with the activation of tanh function having output dimension of size 128 with Batch Normalization is done in order to standardize the input dataset and followed by dropout to avoid any sort of overfitting of the data.
(6) The above data produces the output prediction using sigmoid activation function.
