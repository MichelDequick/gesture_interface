#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('gesture_interface')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Topics
topic_rgb = "camera/rgb/image_raw"
topic_ir1 = "camera/ir1/image_raw"
topic_ir2 = "camera/ir2/image_raw"

topic_opencv_rgb = "gesture_interface/opencv/rgb/image_raw"
topic_opencv_ir1 = "gesture_interface/opencv/ir1/image_raw"
topic_opencv_ir2 = "gesture_interface/opencv/ir2/image_raw"


class image_converter:

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
      cv2.circle(cv_image, (50, 50), 10, 255)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

def main(args):
  ic_rgb = image_converter(topic_rgb, topic_opencv_rgb)
  ic_ir = image_converter(topic_ir1, topic_opencv_ir1)
  ic_ir = image_converter(topic_ir2, topic_opencv_ir2)

  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
