#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('chatter', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 0.5
        pub.publish(msg)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
