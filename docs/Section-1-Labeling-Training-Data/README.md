# Gathering Training Data

1. Gather images from google
    - choose images with a resolution similar to the expected resolution of input images to the detection model
    - ensure there are 100+ instances of each class (object) you wish to detect
    - more diverse images and more images in general means the model will be more robust

2. Use LabelImg to label our dataset
    - ### LabelImg
    - install: https://pypi.org/project/labelImg/
    - draw bounding boxes around objects in images
    - make sure they are given the right class label
    - if using TensorFlow make sure the annotations are in the PascalVoc format (.xml)

3. Use xml_to_csv.py script to change .xml annotations into .csv's
4. Use split_labels.ipynb to split the .csv dataset with all annotations into a test and train .csv
5. Use generate_tfrecord.py to generate a test.record and train.record for TensorFlow