# OpenVINO Model Optimizer
- In order to run models on the Raspberry Pi, they need to be in a .bin .xml format
    - https://docs.openvinotoolkit.org/latest/openvino_docs_MO_DG_Deep_Learning_Model_Optimizer_DevGuide.html
- Download openVINO on a PC. Make sure it has the model_optimizer folder (if RPi install is used it will not include this folder)
- Go to deployment_tools/model_optimizer and run `mo_tf.py --input_meta_graph path_to/model.ckpt.meta --tensorflow_object_detection_api_pipeline_config path_to/pipeline.config --tensorflow_use_custom_config \openvino\deployment_tools_model_optimizer\extensions\front\tf\ssd_support.json`
    - sometimes ssd_v2_support.json must be used
    - this command will output .bin and .xml files
    - If using Windows, you must open cmd as administrator
    - This is for TensorFlow SSD mobilenet models, but model optimizers exist for many different frameworks