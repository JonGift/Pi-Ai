# Using the ArduCAM Camera Module With a Raspberry Pi

For this project, the ArduCAM OBISP MIPI Camera Module was used for testing live video feed when running the custom model on the Pi.
Included in this readme is documentation for setting up the ArduCAM on a Raspberry Pi 4 as well as links to resources that might be useful 
for setting up the camera module.

## Setup Steps
1. Ensure you are running a version of Raspbian that the ArduCAM can support. You can find your kernel version with the command:
```uname -r```
The ArduCAM module supports kernel versions from **4.19.113-v7+** to **5.4.51-v7l+.**

2. Move into a directory that you would like to clone the ArduCAM repo in. Clone the repo with the command:
```
git clone https://github.com/ArduCAM/Arducam_OBISP_MIPI_Camera_Module.git
```

3. Run the install shell script and reboot the Pi. You may need to run the install script as a superuser.

4. Make sure you have the ArduCAM module inserted into the camera feed for the Pi. Otherwise, shutdown your Pi and insert the module. Then, boot it back up.

5. Open a terminal and run the command:
```ls /dev/video*```
to check that you have /dev/video0 output (this is the verification step that you installed the camera driver and your camera is inserted correctly).

6. If you do not see "/dev/video0" as an output on the list, either the camera driver did not install correctly, or the camera module is not inserted correctly. 
Repeat previous steps before continuing. 

7. Update the Pi with the command:
```sudo apt-get update```
**DO NOT upgrade the Rapsberry Pi kernel driver if you have already successfully obtained a kernel version that the ArduCAM supports.**

8. Check your pip3 version install and make sure you are running pip3 v.19+. You may need to install the pip3 package if the command below does not return a version. 
```
pip3 --version
```

9. Install OpenCV and its dependencies using the commands:
```
Insert commands here in future
```

10. If you are not using a virtual environment to install packages, run the command:
```python3 -m pip install v4l2``` to install the python v4l2 module. 

11. At this point, we need to edit the v4l2.py script in two places to ensure that the module works correctly. This is where Resource #2 might be of use. 
```
Insert commands here in future
```

12. If you have successfully completed the previous steps, you should be able to run 
```python3 working_example.py``` from this repo and receive live video feed.


## Helpful Resources
1. https://www.arducam.com/docs/arducam-obisp-mipi-camera-module/3-use-on-raspberry-pi/ 
2. https://bugs.launchpad.net/python-v4l2/+bug/1664158
3. https://www.tensorflow.org/install/pip
4. https://www.arducam.com/docs/camera-for-jetson-nano/mipi-camera-modules-for-jetson-nano/camera-demonstration/
5. https://projects.raspberrypi.org/en/projects/using-pip-on-raspberry-pi
