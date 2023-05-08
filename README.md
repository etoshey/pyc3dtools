# pyc3dtools
This is python package that you can use it to read your c3d file. Actually, this is an [C3Dtools.com](https://c3dtools.com) API.
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
Finally pass the API token and your file path to the readC3D function as an input,
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
import pyc3dtools
import matplotlib.pyplot as plt
import numpy as np

TOKEN = "YOUR_TOKEN"

result =  pyc3dtools.readC3D(TOKEN,'TYPE-2.C3D')

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
plt.plot(Marker1[:,0], color='r', label='X')
plt.plot(Marker1[:,1], color='g', label='Y')
plt.plot(Marker1[:,2], color='b', label='Z')
plt.show()

FZ = np.array(result['ForcePlate'][0]['FZ'])
FZ = FZ.flatten()
plt.plot(FZ)
plt.show()


COP = np.array(result['ForcePlate'][0]['COP'][:][:])
COP_X = COP[:,0,:]
COP_Y = COP[:,1,:]
COP_X = COP_X.flatten()
COP_Y = COP_Y.flatten()


plt.plot(COP_X, color='g', label='copX')
plt.plot(COP_Y, color='b', label='copY')
plt.show()
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


