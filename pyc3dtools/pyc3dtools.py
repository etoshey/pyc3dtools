import requests,json
import numpy as np
import os
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper


def readC3D(Token,file_path): 

    API_URL = "https://c3dtools.com/API/readC3D"   

    data = {'api_key':Token}  

    #r = requests.post(url = API_URL, files=file, data = data)    
    file_size = os.stat(file_path).st_size
    with open(file_path, "rb") as f:
        with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as t:
            wrapped_file = CallbackIOWrapper(t.update, f, "read")
            resp = requests.post(url = API_URL, data= data, files={'upload_file': wrapped_file})   

    try:
        result = json.loads(resp.text) 
        if 'error_msg' in result:
            return({
                'error' : result['error_msg'],
                'Status' : 'Failed'
            })
    
        else:
            return GenerateOutput(result)
            
            
    except Exception as e:
        return({'Status' : 'Failed',
                'error' : e  })
    
def getTRCMot(Token,file_path,des_path):          
    API_URL = "https://c3dtools.com/API/getOpenSimData"
    data = {'api_key':Token}  
    file_name = os.path.basename(file_path)
    file_size = os.stat(file_path).st_size
    with open(file_path, "rb") as f:
        with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as t:
            wrapped_file = CallbackIOWrapper(t.update, f, "read")
            resp=requests.post(url = API_URL, stream=True ,data= data, files={'upload_file': wrapped_file})

    try:
        result = json.loads(resp.text)

        if 'error_msg' in result:
            return({'error' : result['error_msg'] , 'Status' : 'Failed'  })
        else:
            #write to file\
            if 'mot' in result:
                motFile = open(des_path+'/'+file_name[:-3]+'mot','w')
                motFile.writelines(result['mot']['h1'])
                motFile.writelines(result['mot']['h2'])
                for d in result['mot']['data']:
                    motFile.writelines(d)
                motFile.close()
            
            if 'trc' in result:
                trcFile = open(des_path+'/'+file_name[:-3]+'trc','w')
                trcFile.writelines(result['trc']['h1'])
                trcFile.writelines(result['trc']['h2'])
                trcFile.writelines(result['trc']['h3'])
                trcFile.writelines(result['trc']['h4'])
                trcFile.writelines(result['trc']['h5'])
                for d in result['trc']['data']:
                    trcFile.writelines(d)
                trcFile.close()

            return GenerateOutput(result['c3d'])
      
    except Exception as e:
        return({'Status' : 'Failed',
                'error' : e  })

            



def GenerateOutput(result):
    GP =  result["GP"]
    Point = result["Point"]
    Real_marker_index = result["Real_marker_index"]
    Analog = result["Analog"]
    Header = result["Header"]
    Forceplates = result["Forceplate_list"]
    Real_Markers = np.array(Point)
    Markers_lbl = []
    Analog_lbl = []
    Markers_Units = ''
    Markers_XSCREEN = ''
    Markers_YSCREEN = ''


    if len(Point[0]) > 0 :
        Real_Markers = Real_Markers[:,Real_marker_index,:]
        result["Markers"] = Real_Markers

        # List of Markers Label
        gp_point_lbl_i = [
            index for index in range(len(GP))
            if GP[index]['Group_Name'] == 'POINT'
        ][0]    
        gp_point_lbl_ii = [
            index for index in range(len(GP[gp_point_lbl_i]['List_Parameters']))
            if GP[gp_point_lbl_i]['List_Parameters'][index]['Param_Name'] == 'LABELS'
        ][0] 
        gp_point_unit_i = [
            index for index in range(len(GP[gp_point_lbl_i]['List_Parameters']))
            if GP[gp_point_lbl_i]['List_Parameters'][index]['Param_Name'] == 'UNITS'
        ][0] 
        gp_point_Yscreen_i = [
            index for index in range(len(GP[gp_point_lbl_i]['List_Parameters']))
            if GP[gp_point_lbl_i]['List_Parameters'][index]['Param_Name'] == 'Y_SCREEN'
        ][0] 
        gp_point_Xscreen_i = [
            index for index in range(len(GP[gp_point_lbl_i]['List_Parameters']))
            if GP[gp_point_lbl_i]['List_Parameters'][index]['Param_Name'] == 'X_SCREEN'
        ][0] 
        Markers_lbl = GP[gp_point_lbl_i]['List_Parameters'][gp_point_lbl_ii]['Param_data']
        Markers_Units = GP[gp_point_lbl_i]['List_Parameters'][gp_point_unit_i]['Param_data'][0]
        Markers_YSCREEN = GP[gp_point_lbl_i]['List_Parameters'][gp_point_Yscreen_i]['Param_data'][0]
        Markers_XSCREEN = GP[gp_point_lbl_i]['List_Parameters'][gp_point_Xscreen_i]['Param_data'][0]
    

    #List of Analog channel Label
    if len(Analog[0]) > 0 :
        gp_analog_lbl_i = [
            index for index in range(len(GP))
            if GP[index]['Group_Name'] == 'ANALOG'
        ][0]    
        gp_analog_lbl_ii = [
            index for index in range(len(GP[gp_analog_lbl_i]['List_Parameters']))
            if GP[gp_analog_lbl_i]['List_Parameters'][index]['Param_Name'] == 'LABELS'
        ][0] 
        Analog_lbl = GP[gp_analog_lbl_i]['List_Parameters'][gp_analog_lbl_ii]['Param_data']


    
        for f in Forceplates:
                f['Origin'] = f['orgin']     ## SORRY :)
                f['COP'] = np.array(f['COP'][:][:], dtype=object)
                f['GRF_VECTOR'] = np.array(f['GRF_VECTOR'][:][:], dtype=object)           

        
        # convert all analog data to np array
        Analog = np.array(Analog)
        NewAnalog =[]
        for f in Analog:
            main_row = []
            for j in range(int((len(f)/len(Analog_lbl)))-1):
                row = []
                for k in range(j*len(Analog_lbl),(j+1)*len(Analog_lbl)):
                    row.append(f[k])
                main_row.append(row)

            NewAnalog.append(main_row)    

        Analog = np.array(NewAnalog)


    return({
        'Status' : 'Success',
        'GP' : GP,
        'Markers' : Real_Markers,
        'Points' : Point,
        'Analog' : Analog,
        'Header' : Header,
        'ForcePlate' : Forceplates,
        'Markers Label' : Markers_lbl,
        'Analog Label' : Analog_lbl,
        'Units' : Markers_Units,
        'Coordinate system' : [Markers_XSCREEN ,Markers_YSCREEN]
    })







