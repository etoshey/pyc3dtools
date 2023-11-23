import os
import requests,json
import pyc3dtools
import threading
import time
import progressbar

import qtm

TOKEN = ""



menu_id = qtm.gui.insert_menu_submenu(None,"C3Dtools")


def login():
    print("OK!!")


def getAllC3DFiles():
    root = qtm.settings.directory.get_project_directory()   
    allC3d = []
    for path, subdirs, files in os.walk(root+'Data\\'):        
        # Get all C3D files
        files = [f for f in files if ".c3d" in f]
        for name in files:
            print(os.path.join(path, name))
            allC3d.append(os.path.join(path, name))
        
    return allC3d




def C3D2TRC():
    print("111111K!!")
    files = getAllC3DFiles()

    dest_path = os.path.split(files[0])[0]
    print(dest_path)

    x = threading.Thread(target=GetTRCMot_func, args=(files,callable,))   
    x.start()    



def callback(result):
    print("result")

    print(result)



def GetTRCMot_func(files,callback):
    print("progress")

    for f in files:   
        print(f)
        f_name = os.path.split(f)[1]
        qtm.gui.message.add_message("C3Dtools :: "+f_name+ " is uploading... " ,"", "info")
        result = pyc3dtools.getTRCMot_qtm(TOKEN,f,callback)
        print(result['Status'])
        qtm.gui.message.add_message("C3Dtools :: "+result['Status'] ,"", "info")


    

qtm.gui.add_command("C3D2TRC")
qtm.gui.set_command_execute_function("C3D2TRC",C3D2TRC)

qtm.gui.insert_menu_button(menu_id,"C3D to trc (Y-Up)","C3D2TRC")



