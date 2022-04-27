# Traffic Sign Classifier

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

A repository for the road sign classification exercises and project from Udacity's Self-Driving Car Engineer nanodegree. (Project #3)

Due to difficulties installing the correct version of TensorFlow for the project locally, all work on the project was completed in the Udacity online workspace. The files from the finished workspace have been added to the `project/` folder.

Some basic scripts from the lessons and exercises are located in [`scripts/`](./scripts). The images used for those scripts are found in [`images/`](./images). The project, started from the project Udacity repository [here](https://github.com/udacity/CarND-Traffic-Sign-Classifier-Project), is found in [`project/`](./project).

## Project

The goal of this project is to train a convoluational neural net to classify German traffic signs. The dataset contained 43 classes of signs:

![alt text][image1]

After training, the network achieved:
- a training accuracy of 99.9%
- a validation accuracy of 95.8%
- a test accuracy of 93.2%

The network was then tested on five images found on the web:

![alt text][sign1]
![alt text][sign2]
![alt text][sign3]
![alt text][sign4]
![alt text][sign5]

The network classified 2 of the 5 corrctly (40% accuracy), with the following predictions:

![alt text][image5]

An HTML version of the Jupyter notebook for the project can be found in [report.html](./project/report.html)

[//]: # (Image References)

[image1]: ./project/images/data_exploration.png "Visualization of the data set"
[image2]: ./project/images/training_histogram.png "Histogram of training data classes"
[image3]: ./project/images/validation_histogram.png "Histogram of validation data classes"
[image4]: ./project/images/test_histogram.png "Histogram of test data classes"
[image5]: ./project/images/softmax_top5.png "Histogram of top softmax probabilities"
[sign1]: ./project/german_signs/bumps-sm.png "Traffic Sign 1"
[sign2]: ./project/german_signs/caution-sm.png "Traffic Sign 2"
[sign3]: ./project/german_signs/people-working-sm.png "Traffic Sign 3"
[sign4]: ./project/german_signs/snow-sm.png "Traffic Sign 4"
[sign5]: ./project/german_signs/speed-limit-60-sm.png "Traffic Sign 5"