import requests,json
import numpy as np
import os
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper

#API URL
API_URL = "https://c3dtools.com/API/readC3D"
#API_URL = "http://localhost:5001/API/readC3D"

def readC3D(Token,file_path): 

    data = {'api_key':Token}  

    #r = requests.post(url = API_URL, files=file, data = data)    
    file_size = os.stat(file_path).st_size
    with open(file_path, "rb") as f:
        with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as t:
            wrapped_file = CallbackIOWrapper(t.update, f, "read")
            resp = requests.post(url = API_URL, data= data, files={'upload_file': wrapped_file})


    result = json.loads(resp.text) 

    try:
        if 'error_msg' in result:
            return({
                'error' : result['error_msg']
            })
    
        else:
            GP =  result["GP"]
            Point = result["Point"]
            Real_marker_index = result["Real_marker_index"]
            Analog = result["Analog"]
            Header = result["Header"]
            Forceplates = result["Forceplate_list"]
            Real_Markers = np.array(Point)
            Real_Markers = Real_Markers[:,Real_marker_index,:]
            result["Markers"] = Real_Markers


            # COP :: null to 0
            Forceplates


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
            gp_analog_lbl_i = [
                index for index in range(len(GP))
                if GP[index]['Group_Name'] == 'ANALOG'
            ][0]    
            gp_analog_lbl_ii = [
                index for index in range(len(GP[gp_analog_lbl_i]['List_Parameters']))
                if GP[gp_analog_lbl_i]['List_Parameters'][index]['Param_Name'] == 'LABELS'
            ][0] 
            Analog_lbl = GP[gp_analog_lbl_i]['List_Parameters'][gp_analog_lbl_ii]['Param_data']



            ## SORRY :)
            for f in Forceplates:
                 f['Origin'] = f['orgin']            

            return({
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
    except (KeyError):
            return({
                'error' : 'Failed'
            })

    
