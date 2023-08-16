# pyc3dtools 
This is python package that you can use it to read your c3d file. Actually, this is an [C3Dtools.com](https://c3dtools.com) API. 

```diff
- I called it MAHSA
```
The [C3Dtools.com](https://c3dtools.com) is a free web-based biomechanical toolbox.
On [C3Dtools.com](https://c3dtools.com) you can :

        - Lower Body Inverse Kinematic - Plug-in Gait Model NEW
        - Convert C3D file to ASCII and create .TRC and .MOT that is compatible with the Opensim
        - Convert Xsens IMU sensors data to .sto to use in Opensim(Opensens)
        - Detect Gait events based on kinematic data
        - Calculate spatiotemporal gait parameters based on kinematic data
        - Apply Butterworth low-pass and high-pass digital filtering
        - Free C3D files repository
        - Trim C3D file   


# Install
```
pip install pyc3dtools
```




# Usage
First of all, create an account ([Register](https://c3dtools.com/register)) and then log in to your account, you can find the API token on the home page

and then import pyc3dtools package
```python
import pyc3dtools
```
Finally pass the API token and your file path to the readC3D function as inputs,
```python
c3d =  pyc3dtools.readC3D(TOKEN,'TYPE-2.C3D')
```

# Get data
### 1.Header section
```python
Number_of_Markers = c3d['Header']['Number_of_Points']
First_Frame = c3d['Header']['first_frame']
Last_Frame = c3d['Header']['last_frame']
Video_Sampling_Rate = c3d['Header']['Video_Frame_Rate']
Number_of_Analog_Channels = c3d['Header']['Analog_number_channel']
Analog_Sample_Rate = c3d['Header']['Analog_Frame_Rate']
Analog_sample_per_video_frame = c3d['Header']['Analog_sample_per_Frame']
```
#### 2.Marker & Analog Labels
```python
Markers_Label = c3d['Markers Label']
Analog_Label = c3d['Analog Label']
```

#### 3. Markers

```python
### c3d['Markers'][frame][marker][:3]

p1 = c3d['Markers'][0][0][:3] # Get the position of the first marker (x,y,z) in the first frame 
p2 = c3d['Markers'][100][0][:3] # Get the position of the first marker (x,y,z) in the 100th frame
p3 = c3d['Markers'][100][1][:3] # Get the position of the second marker (x,y,z) in the 100th frame
```
#### 5. Units and Coordinate System

```python
Units = c3d['Units']
coordinate_System = c3d['Coordinate system'] #[X_SCREEN, Y_SCREEN]
```

#### 6. ForcePlate Type 2,3,4,5

```python
### c3d['ForcePlate'][Plate Number]['FZ'][Frame][Analog Frame per Video Frame]

Number_Of_Forceplates = len(result['ForcePlate'])
Force = c3d['ForcePlate'][0]['FX'][100] ,c3d['ForcePlate'][0]['FY'][100],c3d['ForcePlate'][0]['FZ'][100] 
Force = c3d['ForcePlate'][0]['FX'][100][10] ,c3d['ForcePlate'][0]['FY'][100][10],c3d['ForcePlate'][0]['FZ'][100][10] 
Corners c3d['ForcePlate'][0]['corners']
Origin = c3d['ForcePlate'][0]['Origin']

### c3d['ForcePlate'][Plate Number]['COP'][Frame][X|Y|Z][Frame][Analog Frame per Video Frame]
Xcop_frame_50_1 = c3d['ForcePlate'][0]['COP'][50][0][1]
Ycop_frame_50_1 = c3d['ForcePlate'][0]['COP'][50][1][1]
Zcop_frame_50_1 = c3d['ForcePlate'][0]['COP'][50][2][1]
```

# Sample
```python

import sys
import pyc3dtools
import matplotlib.pyplot as plt
import numpy as np

TOKEN = "YOUR TOKEN"

result =  pyc3dtools.readC3D(TOKEN,'TYPE-2.C3D')

if result['Status']=='Failed':
  print(f"Failed to Read File... | {result['error']}") 
  sys.exit(0)

print('---------------------------- C3Dtools.Com ----------------------------')
print(f"Header::Number of Markers = {result['Header']['Number_of_Points']}")
print(f"Header::First Frame = {result['Header']['first_frame']}")
print(f"Header::Last Frame = {result['Header']['last_frame']}")
print(f"Header::Video Sampling Rate = {result['Header']['Video_Frame_Rate']}")
print(f"Header::Analog Channels = {result['Header']['Analog_number_channel']}")
print(f"Header:: Analog Sample Rate = {result['Header']['Analog_Frame_Rate']}")
print(f"Header:: Analog sample per video frame = {result['Header']['Analog_sample_per_Frame']}")


print('----------------------------------------------------------------------')
print(f"GP::Markers Label = {result['Markers Label']}")
print(f"GP::Analog Label = {result['Analog Label']}")
print('----------------------------------------------------------------------')
print(f"Markers:: Frame->0 , {result['Markers Label'][0]}  = {result['Markers'][0][0][:3]}")
print(f"Markers:: Frame->100 , {result['Markers Label'][0]}  = {result['Markers'][100][0][:3]}")
print(f"Markers:: Frame->150 , {result['Markers Label'][1]}  = {result['Markers'][150][1][:3]}")
print(f"Markers:: Units = {result['Units']}")
print(f"coordinate System [X_SCREEN, Y_SCREEN] = {result['Coordinate system']}")
print('----------------------------------------------------------------------')
print(f"Number Of Forceplates = {len(result['ForcePlate'])}")
#print(f"First plate:: FX, FY, FZ :: Frame->100 = ({result['ForcePlate'][0]['FX'][100] ,result['ForcePlate'][0]['FY'][100],result['ForcePlate'][0]['FZ'][100] })") # Analog sample per video frame is equal 20 
print(f"First plate:: FX, FY, FZ :: Frame->100 :: Analog Sample 10 = {result['ForcePlate'][0]['FX'][100][10] ,result['ForcePlate'][0]['FY'][100][10],result['ForcePlate'][0]['FZ'][100][10] }") # Analog sample per video frame is equal 20 
print(f"First plate:: Corners = {result['ForcePlate'][0]['corners']}")
print(f"First plate:: Origin = {result['ForcePlate'][0]['Origin']}")
print(f"First plate:: COP :: X,Y,Z :: Frame->50 :: Analog Sample 1 = {result['ForcePlate'][0]['COP'][50][0][1],result['ForcePlate'][0]['COP'][50][1][1],result['ForcePlate'][0]['COP'][50][2][1]}") # Analog sample per video frame is equal 20 



#plot data
Marker1 = result['Markers'][:,1,:3]

FZ = np.array(result['ForcePlate'][0]['FZ'])
FZ = FZ.flatten()


COP = result['ForcePlate'][0]['COP'][:,:,:]
COP_X = COP[:,0,:]
COP_Y = COP[:,1,:]
COP_X = COP_X.flatten()
COP_Y = COP_Y.flatten()


Vec_GRF = result['ForcePlate'][0]['GRF_VECTOR'][:,:,:]
Vec_GRF_X = Vec_GRF[:,0,:]
Vec_GRF_Y = Vec_GRF[:,1,:]
Vec_GRF_Z = Vec_GRF[:,2,:]
Vec_GRF_X = Vec_GRF_X.flatten()
Vec_GRF_Y = Vec_GRF_Y.flatten()
Vec_GRF_Z = Vec_GRF_Z.flatten()


fig = plt.figure()
axs = fig.subplots(2, 2)
axs[0, 0].plot(Marker1[:,0], color='r', label='X')
axs[0, 0].plot(Marker1[:,1], color='g', label='Y')
axs[0, 0].plot(Marker1[:,2], color='b', label='Z')
axs[0, 0].set_title('Marker Position')
axs[0, 1].plot(FZ, 'tab:orange')
axs[0, 1].set_title('GRF Z')
axs[1, 0].plot(COP_X, color='g', label='copX')
axs[1, 0].plot(COP_Y, color='b', label='copY')
axs[1, 0].set_title('COP')
axs[1, 1].plot(Vec_GRF_X, color='g', label='GRFX')
axs[1, 1].plot(Vec_GRF_Y, color='b', label='GRFY')
axs[1, 1].plot(Vec_GRF_Z, color='r', label='GRFZ')
axs[1, 1].set_title('GRF vector')




NumFrames = result['Header']['last_frame'] - result['Header']['first_frame']

Forceplates = result['ForcePlate']
cop_data = []
grf_vector = []
corners = []
for fp in Forceplates:  
  #COP 
  cop_data.append(fp['COP'])
  #GRF
  grf_vector.append(fp['GRF_VECTOR'])
  #Corners
  for c in range(4):    
    corners.extend(fp['corners'])



# COP & GRF
main_cop_data =[]
main_grf_data =[]

for i in range(NumFrames):   
  for fp in range(len(Forceplates)):
    main_cop_data.append([cop_data[fp][i,0,0] , cop_data[fp][i,1,0]])
    main_grf_data.append([grf_vector[fp][i,0,0] , grf_vector[fp][i,1,0], grf_vector[fp][i,2,0]])  



# Get Analog data
Analog_Label = result['Analog Label']
Analog_Data = result['Analog']

ch0 = Analog_Data[:,:,0]
ch1 = Analog_Data[:,:,1]
ch2 = Analog_Data[:,:,2]




plt.show()

print('OK')

```


# Export .mot and .trc
If you need to convert your c3d file to compatible files for OpenSim software you can use *getTRCMot* function. This function returns all c3d file data and also write .mot and .trc file in a directory

```python
import pyc3dtools
TOKEN = "YOUR_TOKEN"
#result =  pyc3dtools.getTRCMot(TOKEN,'Input C3D File','Destination directory')
result =  pyc3dtools.getTRCMot(TOKEN,'TYPE-2.C3D','./exportData')
```

## Export .mot and .trc Sample code
```python
import pyc3dtools
TOKEN = "YOUR_TOKEN"
result =  pyc3dtools.getTRCMot(TOKEN,'TYPE-2.C3D','./exportData')
if result['Status'] == 'Success':
    print('Done.')
```


# Inverse Kinematic : Plug-in Gait
By this API can compute the joint's kinematics. Just pass a static trial, a dynamic trial and anthropometry data of your subject.

```python
import pyc3dtools
import matplotlib.pyplot as plt
import numpy as np

TOKEN = "YOUR TOKEN"

Anthropometry = [('Left_Leg_Length',800), # mm
                  ('Right_Leg_Length',800),
                  ('Knee_Width',100),
                  ('Ankle_Width',90),
                  ('Marker_Radius',14)]


Markers_label = [('LASI','LASI'), # (Fixed label , your label in c3d file)
                 ('RASI','RASI'), # (Fixed label , your label in c3d file)
                 ('LPSI','LPSI'), # (Fixed label , your label in c3d file)
                 ('RPSI','RPSI'), # (Fixed label , your label in c3d file)
                 #('SACR','SACR'), # (Fixed label , your label in c3d file) - Optional
                 ('LTHI','LTHI'), # (Fixed label , your label in c3d file)
                 ('RTHI','RTHI'), # (Fixed label , your label in c3d file)
                 ('LKNE','LKNE'), # (Fixed label , your label in c3d file)
                 ('RKNE','RKNE'), # (Fixed label , your label in c3d file)
                 ('LTIB','LTIB'), # (Fixed label , your label in c3d file)
                 ('RTIB','RTIB'), # (Fixed label , your label in c3d file)
                 ('LANK','LANK'), # (Fixed label , your label in c3d file)
                 ('RANK','RANK'), # (Fixed label , your label in c3d file)
                 ('LHEE','LHEE'), # (Fixed label , your label in c3d file)
                 ('RHEE','RHEE'), # (Fixed label , your label in c3d file)
                 ('LTOE','LTOE'), # (Fixed label , your label in c3d file)
                 ('RTOE','RTOE')] # (Fixed label , your label in c3d file)


#pyc3dtools.IKPiG(TOKEN, Static Trial,Dynamic Trial, Markers_label,Anthropometry,[start Frame, end Frame] *Optional)
result =  pyc3dtools.IKPiG(TOKEN,'Cal 01.C3D','Walking 01.C3D',Markers_label,Anthropometry)



if result['Status'] == 'Success':
    print('Done.')
    t = np.arange(0,len(result['IK_Result'][0]['angle']))  

    fig, axs = plt.subplots(3, 2)
    # HIP Joint
    LHIP = next((obj for obj in result['IK_Result'] if obj['name'] == 'LHIP'),  None)
    RHIP = next((obj for obj in result['IK_Result'] if obj['name'] == 'RHIP'),  None)
    LHIP_angle_x = [item[0] for item in LHIP['angle']]
    LHIP_angle_y = [item[1] for item in LHIP['angle']]
    LHIP_angle_z = [item[2] for item in LHIP['angle']]
    axs[0,0].plot(t,LHIP_angle_x,t,LHIP_angle_y,t,LHIP_angle_z)
    axs[0,0].legend(['Flex/Ext','Abd/Add','Ex/Int Rotation'])
    axs[0,0].set_ylabel('Left HIP')

    RHIP_angle_x = [item[0] for item in RHIP['angle']]
    RHIP_angle_y = [item[1] for item in RHIP['angle']]
    RHIP_angle_z = [item[2] for item in RHIP['angle']]     
    axs[0,1].plot(t,RHIP_angle_x,t,RHIP_angle_y,t,RHIP_angle_z)
    axs[0,1].legend(['Flex/Ext','Abd/Add','Ex/Int Rotation'])
    axs[0,1].set_ylabel('Right HIP')

    # KNEE Joint
    LKNEE = next((obj for obj in result['IK_Result'] if obj['name'] == 'LKNEE'),  None)
    RKNEE = next((obj for obj in result['IK_Result'] if obj['name'] == 'RKNEE'),  None)
    LKNEE_angle_x = [item[0] for item in LKNEE['angle']]
    LKNEE_angle_y = [item[1] for item in LKNEE['angle']]
    LKNEE_angle_z = [item[2] for item in LKNEE['angle']]
    axs[1,0].plot(t,LKNEE_angle_x,t,LKNEE_angle_y,t,LKNEE_angle_z)
    axs[1,0].legend(['Flex/Ext','Abd/Add','Ex/Int Rotation'])
    axs[1,0].set_ylabel('Left Knee')

    RKNEE_angle_x = [item[0] for item in RKNEE['angle']]
    RKNEE_angle_y = [item[1] for item in RKNEE['angle']]
    RKNEE_angle_z = [item[2] for item in RKNEE['angle']] 
    axs[1,1].plot(t,RKNEE_angle_x,t,RKNEE_angle_y,t,RKNEE_angle_z)
    axs[1,1].legend(['Flex/Ext','Abd/Add','Ex/Int Rotation'])
    axs[1,1].set_ylabel('Right Knee')


    # ANKLe Joint
    LANK = next((obj for obj in result['IK_Result'] if obj['name'] == 'LANK'),  None)
    RANK = next((obj for obj in result['IK_Result'] if obj['name'] == 'RANK'),  None)
    LANK_angle_x = [item[0] for item in LANK['angle']]
    LANK_angle_y = [item[1] for item in LANK['angle']]
    LANK_angle_z = [item[2] for item in LANK['angle']]
    axs[2,0].plot(t,LANK_angle_x,t,LANK_angle_y,t,LANK_angle_z)
    axs[2,0].legend(['Flex/Ext','Abd/Add','Ex/Int Rotation'])
    axs[2,0].set_ylabel('Left Ankle')

    RANK_angle_x = [item[0] for item in RANK['angle']]
    RANK_angle_y = [item[1] for item in RANK['angle']]
    RANK_angle_z = [item[2] for item in RANK['angle']] 
    axs[2,1].plot(t,RANK_angle_x,t,RANK_angle_y,t,RANK_angle_z)
    axs[2,1].legend(['Flex/Ext','Abd/Add','Ex/Int Rotation'])
    axs[2,1].set_ylabel('right Ankle')
   

    plt.show()    

```
## Inverse Kinematic Graph
![alt text](http://url/to/img.png)


```diff
+ Women Life Freedom
```