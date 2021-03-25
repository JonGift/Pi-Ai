# Training a Model
1. Use a pretrained model from TensorFlow model zoo (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md)
    - Edit the .config file to point to the training and testing data as well as the .pbtxt file with class names
2. Run the training script (train.py) with the path to the config file
    - EX: `python train.py --train_dir=training-dandelions-and-clovers_relabeled-2/ --pipeline_config_path=ssd_mobilenet_v1_pets.config --logtostderr`
    - Train until the loss reaches an accepted (low) value, but avoid overfitting
3. Freezing a Trained Model
    - Run export_inference_graph.py with the path to the training dir, config file, and the desired model.ckpt file
    - EX: `python export_inference_graph.py --input_type image_tensor --pipeline_config_path training_large_14/ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix training_large_14/model.ckpt-14668 --output_directory graph_large_14`
    - Frozen model will be in the form of a .pb file
    - Use the frozen model in object detection tutorial scripts to test the model performance on various images
        - updated_old_example.py (for images)
        - webcam_detection.py (for video feed)


### Training a Custom Model
Guide for TensorFlow 1:
- https://www.youtube.com/watch?v=C5-SEZ_IvaM&list=PL0AA7mM1J4JtT23k6HFYOCq0EpCFsQi4a&index=8
- https://www.youtube.com/watch?v=_gGI91BmIdk&list=PL0AA7mM1J4JtT23k6HFYOCq0EpCFsQi4a&index=7
- https://github.com/Bengemon825/TF_Object_Detection2020

### Tensorflow GPU install
- install guide: https://www.youtube.com/watch?v=RplXYjxgZbw&list=PL0AA7mM1J4JtT23k6HFYOCq0EpCFsQi4a&index=4
- version compatibility: https://www.tensorflow.org/install/source