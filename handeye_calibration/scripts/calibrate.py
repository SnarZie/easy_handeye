#!/usr/bin/env python

import rospy
from handeye_calibration import HandEyeConnector


def main():
    rospy.init_node('handeye_calibration')
    while rospy.get_time() == 0.0: pass

    hec = HandEyeConnector()

    automatic = rospy.get_param('automatic')
    if automatic:
        hec.spin_automatic()
    else:
        hec.spin_interactive()


if __name__ == '__main__':
    main()
