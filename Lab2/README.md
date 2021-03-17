# Deep Learning on CIFAR-100, using Convolutional Neural Networks and Transfer Learning techinques

## Dataset:

![21](https://user-images.githubusercontent.com/50829499/111316833-4492e680-866c-11eb-8247-010e756a2fcd.png)

The working dataset was [CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html).  It consists of 60000 32x32 colour images in 100 classes (such as vehicles, flowers, household electrical devices, people ...). In this excerisce, our goal was to improre predictions' accuracy on 20 classes

## Description

 The following steps to optimize accuracy, are described below:

### Define Models 

First of all we compare different model architectures about accuarcy <br/>

These architectures were: ***MLP, LeNet, CNN***. <br/>

### Training Proccess

Using different optimizers, (*adam, adamax, SGD*), we train the models, noticing at the same time validation - train accuarcy 

### Evaluation 

Finally we keep the best combination (*model, optimizer*)

### Control and Avoid Overfitting

In order to help our network to generalize to new input data, we follow some steps:

1. *Data augmentation*:  We increase the amount of data by adding slightly modified copies of already existing data so as to avoid overfiting
2. *Adding dropout layers*: It was neccesary since some paths in our network represent noise. So we cancel them using dropout layers.
3. *Early stopping techinques*: During the learning proccess, if the validation accuracy does not improve, we stop learning.
4. Experimentation with learning rate, batch size and different opotimizers

### Transfer Learning

Since we don't have a large dataset, we import VGG-19 network  and we train only the head. Accuracy is incresed by 20 % using Transfer Learning.
