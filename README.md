
[![3Difyme](/images/logo.png?raw=true)](https://3dify.me/)


# Image-To-Pose Converter

This project provides an automated solution for programmers to obtain a corresponding
**3D Aramture and Mesh** with just a **pose image** as an input. The source code is
programmed in [Python](https://www.python.org/) Language which involves invoking through 
[Blender](https://www.blender.org/).

**This program is split in two separate operations:**
- **Part 1:** Obtaining [Mediapipe](https://google.github.io/mediapipe/solutions/pose.html) Mesh
    in OBJ [Wavefront](https://en.wikipedia.org/wiki/Wavefront_.obj_file) format.
- **Part 2:** Mapping the **posed** Mediapipe mesh (obtained in previous step) to [Mixamo](https://www.mixamo.com/) Armature.

## Installation and Setup

- Install [Blender](https://www.blender.org/download/) 3.x or above.
- Install [Python](https://www.python.org/downloads/) 3.7.x or above.
- Install Python Virtual Environment Library [virtualenv](https://pypi.org/project/virtualenv/). 
    Clone this repository, then create and activate a Python Virtual Environment 
    to install necessary libraries.
```
pip install virtualenv
git clone https://github.com/3difyme/image-to-pose.git
cd image-to-pose
virtualenv <name-of-venv>
<name-of-venv>\Scripts\Activate
```
- Install all the dependencies in the Virtual Environment
```
pip install -r requirements.txt
```
**NOTE:** A file named `requirements.txt` should be present in the root directory 
    of your local repository. Otherwise, create a file in the same name and save
    it with the following contents. `protobuf` library is not really required in the
    project, the sole purpose is to downgrade it to version 3.20 to avoid
    compatibility issues.
```
numpy
python-dotenv
opencv-contrib-python
mediapipe
protobuf==3.20
```

## Environment Variables

To run this project, you will need to create a `.env` file in the current directory 
    and update it with the following code below. Assign the value to 
    `BLENDER_PATH` variable.
```
BLENDER_PATH=<path_to_your_blender_exe_file>
``` 
**Eg:**
BLENDER_PATH=C:/Program Files/Blender Foundation/Blender 3.1/blender.exe

## Run Locally

Run the command in the virtual environment by replacing the arguments appropiately.
```
python main.py <IMG_PATH> <INPUT_FBX_PATH> <OUTPUT_FBX_PATH>
```
**NOTE:** There should be two additional files post execution with the following extensions:
- `.obj` file: An intermediate Mediapipe mesh obtained in **Part 1** operation.
- `.fbx` file: Final posed armature obtained in **Part 2** operation.

## Part 1 Implementation

Script: `src/image_to_obj.py`

`create_obj(img, obj_path)` function takes inputs as the pose image and file path
for the mediapipe mesh. The obtained `.obj` file at the given path contains landmarks
at all vertices.

![Image to OBJ Transformation](/images/Part1.png?raw=true)

## Part 2 Implementation

Script: `src/obj_to_armature.py`

The command invokes the above python script through `Blender`, which is executed in `main.py` script.

**Arguments:**

- `import_fbx_path`: Path to an `.fbx` file which should contain one **Mixamo Armature** in Rest Pose.
- `export_fbx_path`: Path to the final `.fbx` file after new pose is applied to the Mixamo Armature.
- `obj_path`: Path to the `.obj` file obtained in **Part 1**.

```
"<BLENDER_PATH>" --background --python src/obj_to_armature.py <import_fbx_path> <export_fbx_path> <obj_path>
```

![OBJ to Armature Pose Transformation](/images/Part2.png?raw=true)

## Authors

- [@rupak-20](https://github.com/rupak-20)
- [@its-just-pritam](https://github.com/its-just-pritam)
- [@bornfree](https://github.com/bornfree)

## Other Links

[![Twitter URL](https://img.shields.io/twitter/url?label=3dify.me&style=plastic&url=https%3A%2F%2F3dify.me%2F)](https://3dify.me/)

[![Instagram](https://img.shields.io/twitter/url?label=Instagram%20%403dify.me&style=plastic&url=https%3A%2F%2F3dify.me%2F)](https://www.instagram.com/3dify.me/)

[![Twitter](https://img.shields.io/twitter/follow/3difyMe?style=social)](https://twitter.com/3difyMe)