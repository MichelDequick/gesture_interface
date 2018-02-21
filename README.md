# Robot-Gesture-Control
ROS, OpenCV, Intel RealSense

## Setup the Up Board
* [Download Ubuntu](http://releases.ubuntu.com/16.04/ubuntu-16.04.3-desktop-amd64.iso)
* Write Ubuntu on the usb stick
* Boot the Up Board from the usb stick
* Install Ubuntu
* Update Ubuntu with folowing commands:
  ```shell
  sudo apt update
  sudo apt -y dist-upgrade
  ```
* Install the linux-upboard kernel with folowing commands:
  ```shell
  sudo add-apt-repository ppa:ubilinux/up
  sudo apt update
  sudo apt -y install linux-upboard
  sudo apt -y autoremove --purge 'linux-.*generic'
  sudo reboot
  ```
* Reboot to ensure you are running the latest software with `sudo reboot`
* Verify you are running the linux-upboard kernel with `uname -r`, the output should be `4.4.0.2-upboard` or higher


## ROS setup on the Up Board
* Adding ROS repository and update Ubuntu package list:
  ```shell
  sudo add-apt-repository http://packages.ros.org/ros/ubuntu
  sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net \
    --recv-key 0xB01FA116
  sudo apt update
  ```
* Installing ROS packages and updating them:
  ```shell
  sudo apt -y install ros-kinetic-desktop-full python-rosinstall ros-kinetic-realsense-camera
  sudo rosdep init
  rosdep update
  echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
  source ~/.bashrc
  ```


## Intel® RealSense™ setup on the Up Board

* Providing kernel source access and installing RealSense™ patches
  ```shell
  wget -q -O - https://bit.ly/en_krnl_src | sudo /bin/bash
  ```

## Install cv_bridge

* Cloning, compiling and installing cv_bridge
  ```shell
  cd ~
  git clone https://github.com/ros-perception/vision_opencv.git
  cd vision_opencv/cv_bridge
  mkdir build && cd build
  cmake ..
  make -j4 && sudo make install
  ```

## Install this repository
* Create a catkin workspace
  ```shell
  mkdir -p ~/catkin_ws/src && cd ~/catkin_ws/src
  git clone https://github.com/MichelDequick/gesture_interface.git
  cd ~/catkin_ws
  catkin_make 
  source devel/setup.bash
  ```


## Running the software
* Reboot to ensure you are running the latest software with `sudo reboot`
* Running the Intel® RealSense™ R200 nodelet
  ```shell
  roscore &
  roscd realsense_camera
  roslaunch realsense_camera r200_nodelet_rgbd.launch
  ```
* Running the ROS visualizer (RViz)
  ```shell
  roscd realsense_camera
  rosrun rviz rviz -d rviz/realsense_rgbd_pointcloud.rviz
  ```

## Other usefull links
* [Instalation guide]("https://01.org/developerjourney/recipe/intel-realsense-robotic-development-kit")
* [Intel Samples for UPBoard]("https://github.com/MichelDequick/realsense_samples_ros")



