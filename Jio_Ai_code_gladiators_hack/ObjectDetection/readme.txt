Description of files:
--------------------------------------------------
1. config: directory contains training and validation configuration.
2. dataset_splitted: contains dataset divided into 3 sets- train, test and validation.
3. images: set of images extracted from all images dataset.
4. data.csv: contains description of bounding boxes for each image.
5. jobs: contains pretrained faster RCNN model.
6. out: contains dataset in form of tensorflow record files (which is used for feeding data to object detection model).
7. scripts: python scripts 

   a) csv_generator.py : parses xml containing bounding box info and generates csv (containing information of images & bounding boxes) and directory (containing images)

   b) dataset_splitter.py : splits dataset generated from csv_generator.py into train, validation and test parts.
   c) video_to_frames_convertor: converts videos to frames.

Steps for training model
---------------------------------------------
1. Download dataset from https://drive.google.com/drive/folders/1yYUiKFUEl-fwB-xNBp9VdPqX7P5bi8be?usp=sharing.
2. Run: python csv_generator.py - it will generate images and data.csv file.
3. Run: python dataset_splitter.py - it will split dataset into train, validation and test parts.
copy train, val, test, train.csv, val.csv and test.csv to parent folder.
4. Run command :
lumi dataset transform --type csv --data-dir . --output-dir out --split train --split val --split test

It will transform dataset into tensorflow records

5. Training object detection model: lumi train -c config/train_config.yml
6. validating model: lumi eval -c config/validation_config.yml
7. Using luminoth web: lumi server web -c train_config.yml



