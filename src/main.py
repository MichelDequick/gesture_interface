#!/usr/bin/env python
from __future__ import print_function
import roslib
roslib.load_manifest('gesture_interface')
import sys
import rospy
from std_msgs.msg import String

import image_converter

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
