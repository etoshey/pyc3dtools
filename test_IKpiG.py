import pyc3dtools
import matplotlib.pyplot as plt
import numpy as np

TOKEN = "YOUR TOKEN"

Anthropometry = [('Left_Leg_Length',800), # mm
                  ('Right_Leg_Length',800),
                  ('Knee_Width',100),
                  ('Ankle_Width',90),
                  ('Marker_Radius',14)]


Markers_label = [('LASI','LASI'),
                 ('RASI','RASI'),
                 ('LPSI','LPSI'),
                 ('RPSI','RPSI'),
                 #('SACR','SACR'), # Optional
                 ('LTHI','LTHI'),
                 ('RTHI','RTHI'),
                 ('LKNE','LKNE'),
                 ('RKNE','RKNE'),
                 ('LTIB','LTIB'),
                 ('RTIB','RTIB'),
                 ('LANK','LANK'),
                 ('RANK','RANK'),
                 ('LHEE','LHEE'),
                 ('RHEE','RHEE'),
                 ('LTOE','LTOE'),
                 ('RTOE','RTOE')]



result =  pyc3dtools.IKPiG(TOKEN,'Cal 01.C3D','Walking 01.C3D',Markers_label,Anthropometry,['50','300'])

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

    a=0