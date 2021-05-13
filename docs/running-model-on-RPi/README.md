# Overview
This README file will explain all the basic steps needed to set up your Raspberry Pi out of the box and install all necessary packages to run the model with a Pi camera component and the NCS2.

## Section 1 - Setting Up The Raspberry Pi 4 
1.	Download the current Raspberry Pi OS With Desktop image and flash a clean microSD with the software using the Raspberry Pi Imager or BalenaEtcher.
https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit. For this project, Kernel version 5.10 was used. 
2. Once the flash finishes, plug the sd card into the Pi and complete the setup process using the "Welcome to Raspberry Pi" setup wizard.
3. After the reboot, open a new terminal and type the command ```sudo raspi-config```. Open "Interface Options" and enable the camera, SSH, and VNC. Back at the main menu, open "Display" and change the resolution to 1920x1080. At this point, select "finish" and reboot the Pi.

## Section 2 - Setting Up And Testing The Raspberry Pi Camera Module
At this point, you should have the camera enabled from step 3 of Section 1. If you did not complete step 3, please do so now. 
1. Shut down your Raspberry Pi and insert the Raspberry Pi camera module. The blue strip will be facing the USB ports.
2. Turn the Pi back on and open a new terminal.
3. Run the command ```raspistill -o ~/Desktop/test.jpg```, if the camera is enabled and inserted correctly, a window will appear with the visible camera field and will snap a test shot that will output to the Desktop. 

## Section 3 - Installing OpenVINO Dependencies And Packages
It might be beneficial to clear up some space on your Pi for this project. So, if you opted for the Raspberry Pi OS with Recommended Software build, execute the following commands to free up some space before continuing:
```
sudo apt-get purge wolfram-engine
sudo apt-get purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove
```
**Dependencies for OpenVINO and OpenCV:**<br>
Note: you can add the -y option after any "sudo apt-get install [-y] \<package\>" to skip the user interaction during the install.
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential cmake unzip pkg-config
```
**Image and Video Libraries:**<br>
```
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
```

**GTK and GTK Warnings:**<br>
```
sudo apt-get install libgtk-3-dev
sudo apt-get install libcanberra-gtk*
```

**Extra Dependencies For OpenCV and Python:**<br>
```
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python3-dev
```

## Section 4 - Downloading OpenVINO
You can choose any directory you would like. For this project, we used the home directory. Modify these commands as needed.<br>
```
cd ~
wget https://download.01.org/opencv/2021/openvinotoolkit/2021.2/l_openvino_toolkit_runtime_raspbian_p_2021.2.185.tgz (check and grab the most current version)
tar -xf l_openvino_toolkit_runtime_raspbian_p_2021.2.185.tgz
mv l_openvino_toolkit_runtime_raspbian_p_2021.2.185 openvino
```

## Section 5 - Setup OpenVINO And NCS2
1. We need to edit the bashrc file to invoke the setupvars.sh script from OpenVINO upon startup. 
```
nano ~/.bashrc
```
Add the following lines to the end of the script:
``` 
# OpenVINO
source ~/openvino/bin/setupvars.sh
```
Exit and save the file, then source the file.
```
source ~/.bashrc
```
2. Next, we need to add the current user to the "users" group on the Pi.
```
sudo usermod -a -G users "$(whoami)"
```
Reboot the Pi.<br>
Once rebooted, open a new terminal and set the USB rules for the NCS2:
```
cd ~
sh openvino/install_dependencies/install_NCS_udev_rules.sh
```
## Section 6 - Build And Run Open Model Zoo Demos
The Open Model Zoo demos are great, but the only ones we could get working were the C++ demos. To build and run the sample demos, continue.
1. Clone the Open Model Zoo GitHub repo:
```
git clone https://github.com/openvinotoolkit/open_model_zoo.git
```
2. The build_demos.sh script did not work for this project, instead we will be building the demos manually.
```
cd open_model_zoo/demos
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-march=armv7-a" ..
make multi_channel_face_detection_demo
```
3. After about 3 minutes, the demo will be ready to use. If you want to build all the demos, instead of ```make multi_channel_face_detection_demo``` you can type only ```make```.
4. (Optional) clone the Pi AI GitHub repo to get our custom models:
```
cd ~
git clone https://github.com/Yamist/Pi-Ai.git
```
5. Now we can move back into the built demo directory
```
cd armv7l/Release
./multi_channel_face_detection_demo -m ~/Pi-Ai/app/models/dandelions-clovers-bindweed-bullthistle-yellowWS/optimized-model/model.ckpt.xml -i 0 -d MYRIAD
```
6. At this point, there will be a new window with the camera feed present. Press "esc" to exit the feed.

## Section 7 - Create A Virtual Environment For OpenVINO (Optional - When Using Python)
This section is not required to run the project demo. You can follow the instructions in this section if you plan to use any Python scripts with OpenVINO or OpenCV demos. 

1. Install pip and two virtual environment packages:<br>
```
cd ~
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip
```
2. Setup virtualenv in the ~/.bashrc
```
nano ~/.bashrc
```
Add the following lines to the end of the bashrc file:
```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
VIRTUALENVWRAPPER_ENV_BIN_DIR=bin
```
3. Exit and save the file. Source it once again ```source ~/.bashrc```
4. Create your first virtual environment:
```
mkvirtualenv openvino -p python3
```
5. Install packages needed for Python scripts:
```
pip install numpy
pip install "picamera[array]"
pip install imutils
pip install opencv-python
```
**Note: Step 4 will automatically activate your openvino virtual environment. To deactivate, simply type "deactivate". To activate, type "workon openvino".**<br>

# What's Next?
At this point our optimized model should be running and making detections on your system. If you'd like to train your own model, please follow the documentation located in the training-custom-model, training-with-gpu, and labeling-training-data folders. Afterwards, you'll need to optimize the model for use with OpenVINO, which can be found in the openVINO-openVINO-model-optimizer folder.