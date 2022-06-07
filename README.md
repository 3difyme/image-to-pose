
<img src="https://3dify.me/images/logo.png" width="100" />



# Image-To-Pose Converter

This project provides an automated solution for posing a [Mixamo](https://www.mixamo.com/) **Armature and Mesh** with just a **pose image** as an input.
You will also need [Blender](https://www.blender.org/) to be able to run the project.


**This program is split in two separate steps:**
- **Part 1:** Obtaining [Mediapipe](https://google.github.io/mediapipe/solutions/pose.html) Mesh
    in OBJ [Wavefront](https://en.wikipedia.org/wiki/Wavefront_.obj_file) format.
- **Part 2:** Mapping the **posed** Mediapipe mesh (obtained in previous step) to [Mixamo](https://www.mixamo.com/) Armature.


## Installation and Setup

- Install [Blender](https://www.blender.org/download/) 3.x or above.
- Install [Python](https://www.python.org/downloads/) 3.7.x or above.

Clone the repo, create a virtualenv, activate it and install the requirements.
```
pip install -r requirements.txt
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
BLENDER_PATH=<PATH_TO_YOUR_BLENDER_BINARY>
``` 
**Eg:** BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 3.1

## Authors

- [@its-just-pritam](https://github.com/its-just-pritam)
- [@rupak-20](https://github.com/rupak-20)
- [@bornfree](https://github.com/bornfree)

## Other Links

[![Twitter URL](https://img.shields.io/twitter/url?label=3dify.me&style=plastic&url=https%3A%2F%2F3dify.me%2F)](https://3dify.me/)

[![Instagram](https://img.shields.io/twitter/url?label=Instagram%20%403dify.me&style=plastic&url=https%3A%2F%2F3dify.me%2F)](https://www.instagram.com/3dify.me/)

[![Twitter](https://img.shields.io/twitter/follow/3difyMe?style=social)](https://twitter.com/3difyMe)
