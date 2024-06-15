#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_publisher():
    rospy.init_node('image_publisher', anonymous=True)
    pub = rospy.Publisher('camera/image', Image, queue_size=10)
    rate = rospy.Rate(10)  # 10hz

    cap = cv2.VideoCapture(0)
    bridge = CvBridge()

    if not cap.isOpened():
        rospy.logerr("Could not open video device")
        return

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            image_message = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            pub.publish(image_message)
        rate.sleep()

    cap.release()

if __name__ == '__main__':
    try:
        image_publisher()
    except rospy.ROSInterruptException:
        pass
