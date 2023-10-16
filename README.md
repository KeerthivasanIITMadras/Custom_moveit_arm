# Custom_moveit_arm

This repository contains a ROS package and URDF file for a custom arm that I have created. The design primarily focuses on controllers and automation algorithm testing, with less consideration for mechanical joint factors. You can simply write a moveit commander to control it with any planner

To run the Gazebo world containing the arm, use the following command:

```bash
roslaunch mrm_description gazebo.launch
```
To launch the moveit planner interface, use the following command:

```bash
roslaunch mrm_moveit moveit_planning_execution.launch
```

The below image shoes how the gazebo world with arm looks(The configuration can be adjusted accordingly, after some forward kinematics planning)

![Screenshot from 2023-10-16 18-58-27](https://github.com/KeerthivasanIITMadras/Custom_moveit_arm/assets/94305617/899e495f-fa43-4e16-97df-43689e1fe24d)

<p>Here is one of the planning executions</p>



https://github.com/KeerthivasanIITMadras/Custom_moveit_arm/assets/94305617/68b9fb1c-0db4-4fff-ab43-b6bfc56078f3

