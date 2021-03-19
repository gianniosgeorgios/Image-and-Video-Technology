# Motion Tracking on Surveillance Videos

## Abstract

Using feature's exraction algorithms, and motion estimation techniques, we detect moving objects inside videos 

## Dataset 

The [VIRAT](https://viratdata.org/) Video Dataset is designed to be realistic, natural and challenging for video surveillance domains in terms of its resolution, background clutter, diversity in scenes, 
and human activity/event categories than existing action recognition datasets. It has become a benchmark dataset for the computer vision community.

## Corner Detection 

First step is of course Corner Detection. Methods tha are used are two: 

* **Harris**: The Harris Corner Detector is just a mathematical way of determining which windows produce large variations when moved in any direction. 
With each window, a score R is associated. Based on this score, you can figure out which ones are corners and which ones are not
* **Shi-Tomasi**: Shi-Tomasi is almost similar to Harris Corner detector, apart from the way the score (R) is calculated.
This gives often a better result. Moreover, in this method, we can find the top N corners, which might be useful in case we don’t want to detect each and every corner

## Optical Flow

Then we are ready to visualize optical flow using Lucas Kande algorithm. The results of our video, show up below: 

