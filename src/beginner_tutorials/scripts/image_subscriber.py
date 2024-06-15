#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def callback(data):
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.imshow("Camera Image", cv_image)
        cv2.waitKey(1)
    except CvBridgeError as e:
        rospy.logerr(e)

def image_subscriber():
    rospy.init_node('image_subscriber', anonymous=True)
    rospy.Subscriber('camera/image', Image, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        image_subscriber()
    except rospy.ROSInterruptException:
        pass
