import pyc3dtools

TOKEN = "YOUR_TOKEN"

result =  pyc3dtools.getTRCMot(TOKEN,'TYPE-2.C3D','./exportData')

if result['Status'] == 'Success':
    print('Done.')