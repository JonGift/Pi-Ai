# Scripts for training and saving a custom model
- train.py 
    - trains model
    - needs a pipeline.config file 
        - which has train.record, test.record, .pbtxt, and path to images in it
    - Ex: `python train.py --train_dir=training-dandelions-and-clovers_relabeled-2/ --pipeline_config_path=ssd_mobilenet_v1_pets.config --logtostderr`

- export_inference_graph.py
    - saves the model to a .pb file so we can use the detection model
    - takes path to a checkpoint file in the training directory
    - Ex: `python export_inference_graph.py --input_type image_tensor --pipeline_config_path training_large_14/ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix training_large_14/model.ckpt-14668 --output_directory graph_large_14`

- updated_old_example.py and webcam_detection.py 
    - given frozen model will run model against either images or real time video and show detection results with a confidence score.