#!/usr/bin/env python
import rospy
import moveit_commander
from geometry_msgs.msg import Pose
import sys
from math import tau

# Here i have to remap the joint states as moveit can only access /joint_states
joint_state_topic = ['joint_states:=/mrm/joint_states']
moveit_commander.roscpp_initialize(joint_state_topic)
rospy.init_node('move_arm')
robot = moveit_commander.RobotCommander()
group = moveit_commander.MoveGroupCommander("arm")
moveit_commander.roscpp_initialize(sys.argv)

# joint_goal = group.get_current_joint_values()
# print(joint_goal)
# joint_goal[0] = 1.2
# joint_goal[1] = -tau / 8
# joint_goal[2] = 0
# joint_goal[3] = -tau / 4
# joint_goal[4] = 0


# group.go(joint_goal, wait=True)


# group.stop()


pose_goal = Pose()
pose_goal.orientation.w = 1.0
pose_goal.position.x = 0.2
pose_goal.position.y = 0.2
pose_goal.position.z = 3
group.set_pose_target(pose_goal)

plan = group.go(wait=True)
# Calling `stop()` ensures that there is no residual movement
group.stop()
# It is always good to clear your targets after planning with poses.
# Note: there is no equivalent function for clear_joint_value_targets()
group.clear_pose_targets()
