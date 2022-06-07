
[![3Difyme](https://3dify.me/images/logo.png)](https://3dify.me/)



# Image-To-Pose Converter

This project provides an automated solution for programmers to obtain a corresponding
**3D Aramture and Mesh** with just a **pose image** as an input. The source code is
programmed in [Python](https://www.python.org/) Language which involves invoking through 
[Blender](https://www.blender.org/).

**NOTE:** This application is developed in a Windows Platform inside a 
Python Virtual Environment. 

**This program is split in two separate steps:**
- **Part 1:** Obtaining [Mediapipe](https://google.github.io/mediapipe/solutions/pose.html) Mesh
    in OBJ [Wavefront](https://en.wikipedia.org/wiki/Wavefront_.obj_file) format.
- **Part 1:** Mapping the **posed** Mediapipe mesh (obtained in previous step) to [Mixamo](https://www.mixamo.com/) Armature.

## Important Links

[![Twitter URL](https://img.shields.io/twitter/url?label=3dify.me&style=plastic&url=https%3A%2F%2F3dify.me%2F)](https://3dify.me/)

[![Instagram](https://img.shields.io/twitter/url?label=Instagram%20%403dify.me&style=plastic&url=https%3A%2F%2F3dify.me%2F)](https://www.instagram.com/3dify.me/)

[![Twitter](https://img.shields.io/twitter/follow/3difyMe?style=social)](https://twitter.com/3difyMe)

## Installation and Setup

- Install [Blender](https://www.blender.org/download/) 3.x or above.
- Install [Python](https://www.python.org/downloads/) 3.7.x or above.
- Install Python Virtual Environment Library [virtualenv](https://pypi.org/project/virtualenv/).
```
pip install virtualenv
```
- Clone this repository or download it directly from Github and unzip it.
- Open a terminal in the root directory in the local repository and create and activate a 
    Python Virtual Environment to install necessary libraries.
```
virtualenv <name-of-venv>
<name-of-venv>\Scripts\Activate
```
- Install all the dependencies in the Virtual Environment
```
pip install -r requirements.txt
```
**NOTE:** A file named `requirements.txt` should be present in the root directory 
    of your local repository. Otherwise, create a file in the same name and save
    it with the following contents.
```
numpy
python-dotenv
opencv-contrib-python==4.5.5.64
mediapipe==0.8.10
```
Incase you come across any issue while installing the above packages due to compatibility
issues with the `protobuf` library, then downgrade it to a lower version.
```
protobuf==3.20.0
```

## Environment Variables

To run this project, you will need to create a `.env` file in the current directory 
    and update it with the following code below. Assign the path of your installed
    Blender directory to `BLENDER_PATH` variable.
```
BLENDER_PATH=<PATH_TO_YOUR_BLENDER_ROOT_DIRECTORY>
``` 
**Eg:** BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 3.1

## Authors

- [@bornfree](https://github.com/bornfree)
- [@its-just-pritam](https://github.com/its-just-pritam)
- [@rupak-20](https://github.com/rupak-20)