import os
import pyc3dtools
import threading
import qtm

# Public Token
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2Njc0MTM1MDYzNzY4NTYzIiwiaWF0IjoxNzAwOTk0MjY2LCJleHAiOjE3MDA5OTc4NjZ9.g18Ch69qRYe2MMcT0n7W3DHOeSnNXi8iF__GdeUQ1a0"


menu_id = qtm.gui.insert_menu_submenu(None,"C3Dtools")


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
    files = getAllC3DFiles()

    if len(files)==0:
        qtm.gui.message.add_message("C3Dtools :: C3D files not found!","", "info")
    else:
        x = threading.Thread(target=GetTRCMot_func, args=(files,callback,))
        x.start()    



def callback(result):
    # TODO :: update UI
    print('callback')





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

qtm.gui.insert_menu_button(menu_id,"C3D to Opensim","C3D2TRC")



