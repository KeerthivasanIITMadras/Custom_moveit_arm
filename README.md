# Custom_moveit_arm

This repository contains a ROS package and URDF file for a custom arm that I have created. The design primarily focuses on controllers and automation algorithm testing, with less consideration for mechanical joint factors.

To run the Gazebo world containing the arm, use the following command:

```bash
roslaunch mrm_description gazebo.launch
```
To launch the moveit planner interface, use the following command:

```bash
roslaunch mrm_moveit moveit_planning_execution.launch
```
