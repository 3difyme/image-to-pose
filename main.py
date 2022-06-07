import os
import sys
from dotenv import load_dotenv

if __name__ == '__main__':

    load_dotenv()
    img_path, import_fbx_path, export_fbx_path = sys.argv[1], sys.argv[2], sys.argv[3]
    blender_path = os.getenv('BLENDER_PATH')
    obj_path = os.getenv('MEDIAPIPE_OBJ_NAME')
    
    os.system('python image_to_obj.py ' + img_path + ' ' + obj_path)
    print('++++ Part 1: Mediapipe mesh obtained from pose image')

    blender_invoke_command = '"' + blender_path + '"' + ' --background --python ' + 'obj_to_armature.py ' + import_fbx_path + ' ' + export_fbx_path + ' ' + obj_path
    print(blender_invoke_command)
    os.system(blender_invoke_command)
    print('++++ Part 2: Posed armature obtained from Mediapipe mesh.')