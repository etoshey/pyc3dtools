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

print('OK')