# Pi-Ai Object Detection Model
Senior Capstone repo for integrating Raspberry Pi and neural computing stick for real time image processing

#### Development Dependencies
* Anaconda

#### Run the app locally:
1. Clone the repo.
2. Run `conda env create -f env.yml`
3. Run `conda activate piai-env`
4. Run `piai.py`

#### Exporting yml environment
Run `conda env export > env.yml`


## Pipeline

1. Gather training images
2. Annotate training images using labelImg to get Pascal Voc format (.xml)
3. use xml_to_csv.py to convert .xml annotations to .csv format
4. Make test.record and train.record for Tensorflow to use in training
5. Make a object_detection.pbtxt with labels
6. Set paths and hyperparameters in pipeline.config file
7. Train model using Tensorflow (train.py)
8. View training results in Tensorboard
9. Create frozen model (export_inference_graph.py)
10. Run model on set of images (object_detection_tutorial.ipynb)
11. Make adjustments to pipeline.config, add training images, retrain
12. Put frozen model on USB, connect to RPi, copy frozen model to RPi
13. Use openVINO model optimizer to convert frozen_inference_graph.pb file to RPi compatible format
14. Run model on RPi using Pi camera
15. From drone, connect battery and use remote connection
16. View results in real time

![alt text](https://github.com/Yamist/Pi-Ai/blob/master/docs/system-diagram.png)

## Resources

### openVINO: 
- model optimizer: https://docs.openvinotoolkit.org/latest/openvino_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_TensorFlow.html
- install for RPi: https://docs.openvinotoolkit.org/latest/openvino_docs_install_guides_installing_openvino_raspbian.html

### TensorFlow
- model zoo: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md
- install: https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/

### LabelImg
- install: https://pypi.org/project/labelImg/

### Tensorflow GPU install
- install guide: https://www.youtube.com/watch?v=RplXYjxgZbw&list=PL0AA7mM1J4JtT23k6HFYOCq0EpCFsQi4a&index=4
- version compatibility: https://www.tensorflow.org/install/source

### Training a Custom Model
Guide for TensorFlow 1:
- https://www.youtube.com/watch?v=C5-SEZ_IvaM&list=PL0AA7mM1J4JtT23k6HFYOCq0EpCFsQi4a&index=8
- https://www.youtube.com/watch?v=_gGI91BmIdk&list=PL0AA7mM1J4JtT23k6HFYOCq0EpCFsQi4a&index=7
- https://github.com/Bengemon825/TF_Object_Detection2020



