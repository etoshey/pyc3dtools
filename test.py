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


plt.show()

print('OK')