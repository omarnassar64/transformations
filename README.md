# 🚗🤖 AE86 Bot & Transformations – Robotics Training 2025

---

## 📌 Overview
This repository contains the solutions for **Electrical M.I.A. Robotics Task 1 (2023/24 & 2025)**.  

It includes two main parts:

- **AE86 Bot Simulation** (URDF/XACRO + ROS + RViz/Gazebo).  
- **3D Transformations with Homogeneous Transformation Matrices (HTM) in Python**.  

---

## 🛠 Requirements

### 🔹 For the Robot (ROS side)
- Ubuntu with **ROS Noetic** (recommended).  
- ROS packages:  
  - `urdf`  
  - `xacro`  
  - `rospy`  
  - `std_msgs`  
  - `rviz`  
  - `gazebo_ros`  

### 🔹 For the Python Transformation
- Python 3.x  
- Install dependencies:  
  `bash
pip install numpy matplotlip`

---

## ⚙️ Part 1: AE86 Bot Simulation

### ▶️ Build & Run
`cd ~/catkin_ws`
`catkin_make`
`source devel/setup.bash`
`roslaunch ae86_bot display.launch`

## 📂 Files

ae86_bot/urdf/ae86_bot.xacro → URDF/XACRO robot description.

ae86_bot/launch/display.launch → Launch file for RViz.

ae86_bot/launch/gazebo.launch → Launch file for Gazebo.

CMakeLists.txt & package.xml → Catkin build files


---

## ⚙️ Part 2: 3D Transformations (HTM)

## 📂 Files  

- `transformation.py` → Python implementation of HTM transformations.  


## ▶️ Run Instructions  

`bash
cd ~/transformations
python3 transformation.py`

## ⌨️ Example Input

Enter number of points: 2
Enter point 1 (x y z): 0 0 5
Enter point 2 (x y z): 2 1 0
Enter translation (tx ty tz): 1 0 -2
Enter rotation angles (θx θy θz) in degrees: 30 45 45

## 🖥 Output  

- Script prints **transformed coordinates**.  
- Matplotlib 3D plot displays:  
  - 🔵 **Blue** → Original points.  
  - 🔴 **Red** → Transformed points.  

---

## 📚 Theory Recap  

**Homogeneous Transformation Matrix (HTM)** is a **4×4 matrix** combining rotation and translation:  

\[
T =
\begin{bmatrix}
R & t \\
0 & 1
\end{bmatrix}
\]

Where:  
- \( R \) → 3×3 rotation matrix.  
- \( t \) → 3×1 translation vector.  



