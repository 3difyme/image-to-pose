import os
import sys
from cv2 import imread
from dotenv import load_dotenv

from src.image_to_obj import create_obj

if __name__ == '__main__':

    load_dotenv()
    if len(sys.argv) < 4:
        print('expected 3 additional arguments, passed', len(sys.argv) - 1)
        print('expected "python main.py <IMG_PATH> <INPUT_FBX_PATH> <OUTPUT_FBX_PATH>"')

    elif len(sys.argv) > 4:
        print('expected 3 additional arguments, passed', len(sys.argv) - 1)
        print('expected "python main.py <IMG_PATH> <INPUT_FBX_PATH> <OUTPUT_FBX_PATH>"')

    else:
        img_path, import_fbx_path, export_fbx_path = sys.argv[1], sys.argv[2], sys.argv[3]
        blender_path = os.getenv('BLENDER_PATH')
        obj_path = 'mediapipe_mesh.obj'

        img = imread(img_path)
        create_obj(img, obj_path)
        print('++++ Part 1: Mediapipe mesh obtained from ' + img_path, end='\n\n')

        blender_invoke_command = '"' + blender_path + '"' + ' --background --python ' + 'src/obj_to_armature.py ' + import_fbx_path + ' ' + export_fbx_path + ' ' + obj_path
        os.system(blender_invoke_command)
        print('\n++++ Part 2: Posed FBX written to ' + export_fbx_path)
