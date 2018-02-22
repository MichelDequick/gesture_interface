#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('gesture_interface')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Topics
topic_rgb = "camera/rgb/image_raw"
topic_data = "person_tracking_output"



class image_converter:

  def __init__(self, topic,  encoding):
    self.encoding = encoding
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber(topic, Image, self.callback)

  def callback(self, data):
    try:
      data.encoding = self.encoding
      
      cv_image = self.bridge.imgmsg_to_cv2(data, self.encoding)
    except CvBridgeError as e:
      print(e)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

class wave_recognition:

  def __init__(self, topic):
    self.data_sub = rospy.Subscriber(topic, String, self.callback)

  def callback(self, data):
    try:
      self.elbow_left = ""
      self.elbow_right = ""
    except CvBridgeError as e:
      print(e)

    cv2.circle(cv_image, (200, 200), 0, 255)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)


def main(args):
  ic_rgb = image_converter(topic_rgb, "bgr8")
  #wr = wave_recognition(topic_data)
  
  rospy.init_node('image_converter', anonymous=True)
  rospy.init_node('wave_recognition', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
