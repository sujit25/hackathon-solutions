# Reliance Jio AI code gladiators hackathon - 2019
contest url: https://www.techgig.com/codegladiators/artificial-intelligence

## Problem statement: Given a parking lot image, predict possible parking locations for vehicles.

## Solutions contains 2 approaches:
1. ImageClassifier - Trained CNN from scratch using keras (tensorflow backend) for classifying patch of parking images into 2 classes -busy/free slot.
2. ObjectDetection - Trained FasterRCNN for identifying possible parking locations in given parking image and predicting its availability. Faster RCNN model has been trained using opensource tool Luminoth(https://luminoth.ai/).

All files (including model, presentation, data etc) for approach 2 can be downloaded from http://tiny.cc/mwobaz 

## References
- Dataset url: http://cnrpark.it/dataset/CNRPark-Patches-150x150.zip
- reference papers: - http://www.sciencedirect.com/science/article/pii/S095741741630598X
                  - http://ieeexplore.ieee.org/abstract/document/7543901/
