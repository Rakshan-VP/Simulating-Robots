# 🤖 Simulating-Robots

[![Webots Version](https://img.shields.io/badge/Webots-R2025a-blue.svg)](https://cyberbotics.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10.9-yellow.svg)](https://www.python.org/downloads/release/python-3109/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A collection of interactive robot simulations using Webots and Python.  
Features real-time control through an integrated PyQt5 GUI built into each robot controller.

## 🔧 Specifications

The following tools and libraries are used in this repository:

- **Webots**: `R2025a`  
  > Robot simulator used for 3D physics-based simulations.

- **Python**: `3.10.9`  
  > Main programming language for writing controllers and GUI.

- **PyQt5**: `>=5.15`  
  > For building the GUI interface (embedded within controller).

- **NumPy**: `>=1.21`  
  > For numerical operations and matrix handling.

- **Matplotlib**: `>=3.5` *(optional)*  
  > Used for plotting if needed (e.g., data visualization from sensors).



## 📦 Generic Project Structure

```
Simulating-Robots/
├── My Robot/
│   ├── worlds/
│   │   └── world.wbt
│   ├── controllers/
|   |   └── controller
│   │       └── controller.py   # Includes both controller logic and GUI
│   └── meshes/
|       ├── mesh1.obj
|       └── mesh2.obj
└── README.md

```


## 🔧 Requirements

- [Webots R2025a](https://cyberbotics.com/)
- Python 3.10.9
- PyQt5
- numpy, matplotlib, etc.


## 🧪 How to Run Simulations

### 🌍 Step 1: Open a `.wbt` World in Webots

- Navigate to any of the `worlds/` directories (e.g., `1 Differential Mobile Robot/worlds`)
- Open the `.wbt` file in Webots:
  - Example: `differential_robot_world.wbt`

### 🕹️ Step 2: Run the Python Controller (includes GUI)

- Ensure the `controller` field in your robot node is set to the controller you are using.
- Press the **play** button in Webots
- A PyQt5 GUI will appear (embedded in the controller), which can be used to control and monitor the robot in real-time.


## 💻 Writing Your Own Code

If you'd like to modify or extend the controller/GUI:

1. Open the corresponding `.py` file in `controllers/`
2. Example:
    ```bash
    cd 1\ Differential\ Mobile\ Robot\controllers
    nano controller.py
    ```
3. Edit the logic or GUI as needed — both are in the same script.



## 📌 Notes

- Use **SI units** (meters, seconds, kilograms) in all Webots models.
- The GUI and robot logic are part of the same Python controller file.
- Ensure Webots allows launching GUI apps from controllers (check system permissions or use X11 if on Linux).



## 🪪 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## 🌐 Links

- Webots: [https://cyberbotics.com](https://cyberbotics.com)
- PyQt5: [https://pypi.org/project/PyQt5/](https://pypi.org/project/PyQt5/)
