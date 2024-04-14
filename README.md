# Pneumonia_Classifier

## Identifying medical diagnoses and treatable diseases by image-based deep learning:  
### Object:
In this project, we train a deep learning model that detects viral pneumonia based on chest X-rays. 
The input is an image-like data and the task is a computer-vision subject.

### Development:
The input data contains two types of images, Pneumonia, and normal. These are the two categories of X-rays that the model
will learn and predict. Also, having a relatively important size of data, we decide to use it to train a Convolutional Neural
Network from scratch. Some data augmentation techniques are used to increase the size of the dataset.   
The notebook ``notebooks/cnntrainingcolab.ipynb`` contains the main code to train the deep learning model.  
Some additional scripts were added to deal with several points, like downloading and preparing data.

### Context:
- [Context of the subject](https://www.cell.com/cell/fulltext/S0092-8674(18)30154-5)
- [Data](https://data.mendeley.com/datasets/rscbjbr9sj/2?__hstc=25856994.9f1ad2e8f43bfb04214451e022ace5e2.1713104000275.1713104000275.1713104000275.1&__hssc=25856994.1.1713104000275&__hsfp=856257562)

### Build and Install:
clone the repository, create a virtual environment and install the dependencies.  
For windows users, you can run the following commands:
-  ``git clone https://github.com/deepanshu-yadav/Pneumonia_Classifier.git`` 
- ``python -m virtualenv .venv``
- ```.venv\Scripts\activate```
- ``pip install -r  .\requirements.txt``

### Testing the model
The trained CNN is saved in a ``.H5`` file that can be used to test some X-ray images.  
The notebook ``notebooks/cnntesting.ipynb`` shows how to load the trained model and test it on some sample data.
