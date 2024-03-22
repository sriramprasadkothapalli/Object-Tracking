## Object-Tracking

This README provies guidlines for running the object tracking code.

# Libraries 
Install these libraries
```
import os
from google.colab import drive
from google.colab.patches import cv2_imshow
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

```
# Execution Instructions 
- Read the video and extract individual frames using OpenCV
- Loop over each frame to extract the pixels of moving object 
- Calculate the centroid of the object in every frame
- Assume TOP LEFT corner of the frame as 0,0 and accordingly use ‘Standard Least Square’ to fit a curve (parabola)
- Given that x axis value is 1000, find the y axis value for calculated equaton
- Capture any one frame from the video (which shows the object) and plot the obtained equation

# Results

- The results are visualized in the images below:
![image](https://github.com/sriramprasadkothapalli/Object-Tracking/assets/143056659/ddf21d8e-e363-4919-a440-cdace02ffdc4)
![image](https://github.com/sriramprasadkothapalli/Object-Tracking/assets/143056659/9b325a28-adab-450a-800e-e401633e4a3b)
