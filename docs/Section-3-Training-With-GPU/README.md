# How to use TensorFlow GPU
TensorFlow GPU is compatible with NVIDIA GPUs
- This site describes all the packages needed for TensorFlow GPU: https://www.tensorflow.org/install/source#gpu
- The packages needed are:
    - cuDNN
    - CUDA
    - Python
    - GCC Compiler

- For this project, the following environment was used:
    - TensorFlow 1.14
    - cudatoolkit 10.0.130
    - cudnn 7.6.5
    - NVIDIA GeForce GTX 1660 Ti 

- This video describes the install process
    - https://www.youtube.com/watch?v=RplXYjxgZbw&list=PL0AA7mM1J4JtT23k6HFYOCq0EpCFsQi4a&index=4

- During training
    - CUDA out of Memory Error: decrease batch size in config file
