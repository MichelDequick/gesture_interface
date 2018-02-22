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
topic_depth = "camera/depth/image"

topic_opencv_rgb = "gesture_interface/opencv/rgb/image_raw"
topic_opencv_depth = "gesture_interface/opencv/depth/image"



class rgb_image_converter:

  def __init__(self, topic_in, topic_out):
    self.image_pub = rospy.Publisher(topic_out, Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber(topic_in, Image, self.callback)

  def callback(self, data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    (rows, cols, channels) = cv_image.shape
    if cols > 60 and rows > 60:
      cv2.circle(cv_image, (150, 150), 50, 255)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

class depth_image_converter:

  def __init__(self, topic_in, topic_out):
    self.image_pub = rospy.Publisher(topic_out, Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber(topic_in, Image, self.callback)

  def callback(self, data):
    try:
      cv_image = self.bridge.normalize(data,  cv_image, 1, 0, cv.NORM_MINMAX)
      cv_image = self.bridge.imgmsg_to_cv2(cv_image, "32FC1")
    except CvBridgeError as e:
      print(e)

    (rows, cols, channels) = cv_image.shape
    if cols > 60 and rows > 60:
      cv2.circle(cv_image, (150, 150), 50, 255)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

#    try:
#      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
#    except CvBridgeError as e:
#      print(e)

def main(args):
  ic_rgb = rgb_image_converter(topic_rgb, topic_opencv_rgb)
  ic_depth = depth_image_converter(topic_depth, topic_opencv_depth)

  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
