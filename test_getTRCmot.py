import pyc3dtools

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIyNjU4NTM0NDg3NzQ2MDM0IiwiaWF0IjoxNjc5OTE4NDY1LCJleHAiOjE2Nzk5MjIwNjV9.IDZAmMoneWqw6rjlmpl15ZpjbgDjtQFhYwI_iy1uX6E"

result =  pyc3dtools.getTRCMot(TOKEN,'Walking 01.C3D','./exportData')

if result['Status'] == 'Success':
    print('Done.')