import os
import sys

if __name__ == '__main__':
    img_path, import_fbx_path, export_fbx_path = sys.argv[1], sys.argv[2], sys.argv[3]
    obj_path = 'mediaPipe_mesh.obj'
    path = 'C:\\Users\\Rupak\\Documents\\Study\\Placement\\Internship\\PixelHash\\Task-5\\'
    varpath = 'C:/Users/Rupak/Documents/Study/Placement/Internship/PixelHash/Task-5/'
    blender_path = 'blender.exe --background --python ' + 'task5b.py ' + import_fbx_path + ' ' + export_fbx_path + ' ' + obj_path
    print(blender_path)
    
    os.system('python task5a.py ' + img_path + ' ' + obj_path)
    print('5a done')
    # print(os.getcwd())
    os.system(blender_path)
    print('5b done')
    # try:
    #     print("Inserting inside-", os.getcwd())
    #     os.chdir('C:/Program Files/Blender Foundation/Blender 3.1/')
    #     print(os.getcwd())
    #     os.system(blender_path)
    #     print('5b done')
    # # Caching the exception    
    # except:
    #     print("Something wrong with specified directory. Exception- ")
    #     print(sys.exc_info())