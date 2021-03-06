# **Traffic Sign Recognition** 

## Writeup

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./images/data_exploration.png "Visualization of the data set"
[image2]: ./images/training_histogram.png "Histogram of training data classes"
[image3]: ./images/validation_histogram.png "Histogram of validation data classes"
[image4]: ./images/test_histogram.png "Histogram of test data classes"
[image5]: ./images/softmax_top5.png "Histogram of top softmax probabilities"
[sign1]: ./german_signs/bumps-sm.png "Traffic Sign 1"
[sign2]: ./german_signs/caution-sm.png "Traffic Sign 2"
[sign3]: ./german_signs/people-working-sm.png "Traffic Sign 3"
[sign4]: ./german_signs/snow-sm.png "Traffic Sign 4"
[sign5]: ./german_signs/speed-limit-60-sm.png "Traffic Sign 5"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one. You can submit your writeup as markdown or pdf. You can use this template as a guide for writing the report. The submission includes the project code.

You're reading it! and here is a link to my [project code](https://github.com/udacity/CarND-Traffic-Sign-Classifier-Project/blob/master/Traffic_Sign_Classifier.ipynb)

### Data Set Summary & Exploration

#### 1. Provide a basic summary of the data set. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

I used the numpy library to calculate summary statistics of the traffic signs data set:

* The size of training set is 34799.
* The size of the validation set is 4410.
* The size of test set is 12630.
* The shape of a traffic sign image is (32, 32, 3).
* The number of unique classes/labels in the data set is 43.

#### 2. Include an exploratory visualization of the dataset.

Here is an exploratory visualization of the data set. For each class, it displays the number, label, and a random image form that class.

![alt text][image1]

The following histograms show that the distribution of classes is reasonably consistent between the training, validation, and test datasets.

![alt text][image2]
![alt text][image3]
![alt text][image4]



### Design and Test a Model Architecture

#### 1. Describe how you preprocessed the image data. What techniques were chosen and why did you choose these techniques? Consider including images showing the output of each preprocessing technique. Pre-processing refers to techniques such as converting to grayscale, normalization, etc. (OPTIONAL: As described in the "Stand Out Suggestions" part of the rubric, if you generated additional data for training, describe why you decided to generate additional data, how you generated the data, and provide example images of the additional data. Then describe the characteristics of the augmented training set like number of images in the set, number of images for each class, etc.)

My preprocessing included two steps.

First, I decided to convert the images to grayscale because the important part of the sign is the shapes the compose it and the contrast between the sections, less so the actual colour of it. Colorbling people can read road signs just fine.

Second, I normalized the image data to give it zero mean and zero variance.

#### 2. Describe what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

My final model consisted of the following layers:

| Layer 				|     Description								| 
|:---------------------:|:---------------------------------------------:| 
| Input					| 32x32x1 grayscale image 						| 
| Convolution			| 1x1 stride, valid padding, outputs 28x28x6	|
| RELU					|												|
| Max pooling			| 2x2 stride, valid padding, outputs 14x14x6	|
| Convolution			| 1x1 stride, valid padding, outputs 10x10x16	|
| RELU					|												|
| Max pooling			| 2x2 stride, valid padding, outputs 5x5x16		|
| Flatten				| Outputs 400 									|
| Fully connected		| Outputs 120									|
| RELU					|												|
| Dropout				| Keep prob = 65%								|
| Fully connected		| Outputs 84									|
| RELU					|												|
| Dropout				| Keep prob = 65%								|
| Fully connected		| Outputs 43									|

#### 3. Describe how you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

To train the model, I used a batch size of 50 for 30 epochs, and a learning rate of 0.0008. The mu was 0 and the sigma was 0.1. I used the Adam optimiser.

#### 4. Describe the approach taken for finding a solution and getting the validation set accuracy to be at least 0.93. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

My final model results were:
* training set accuracy of 0.999.
* validation set accuracy of 0.958.
* test set accuracy of 0.932.

The architecture I chose was inspired largely by the neural network built with Keras in lesson 16, with some added layers because a common theme in a review of other networks was that deeper networks tended to perform pretty well. I added some dropout to help increase the learning, which tended to increase the validation accuracy on average from ~92-93% to ~95-96%. I played a bit with the keep probability and it seemed that 65% was better than 50%, but past 65% it didn't seem to improve. The epochs and the batch size were played with a bit but no conclusive results seemed to come out of it.

### Test a Model on New Images

#### 1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are five German traffic signs that I found on the web:

![alt text][sign1] ![alt text][sign2] ![alt text][sign3] 
![alt text][sign4] ![alt text][sign5]

The first image might be difficult to classify because of the light background and the worded sign below.

The second image might be difficult to classify because of the washed-out colouring, and again the sign below.

The third image may be difficult to classify because in other examples of that sign, there's some padding between the person working and the red border, but in this sign there is no space.

The fourth image may be difficult to classify because of some light reflected on the sign.

The fifth image may be difficult to classify because of the washed-out quality and some grainy gray pixels between the 6 and the 0.

#### 2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

Here are the results of the prediction:

| Image					|     Prediction										| 
|:---------------------:|:-----------------------------------------------------:| 
| Bumpy road			| No passing											| 
| General caution		| General caution										|
| Road work 			| Road work												|
| Beware of ice/snow	| Speed limit (100km/h)									|
| Speed limit (60km/h)	| Speed limit (50km/h)									|


The model was able to correctly guess only 2 of the 5 traffic signs, which gives an accuracy of 40%. This is much less than the success of the test set, which scored over 93%.

#### 3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

Here are histograms for the predictions of the top 5 softmax probabilities for each of the new images.


![alt text][image5]
