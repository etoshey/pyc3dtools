
% Solve plug-in gait for lower body by C3Dtools.com
% Soroosh.b.k

%% Send Post Request
% parameters { token , labels , Anthropometry , staic file, dynamic file }

uri = 'https://c3dtools.com/API/IKPiG';
token = "Your_Token";

% LASI,your lbl/RASI,your lbl/....
Markers_label = 'LASI,LASI/RASI,RASI/LPSI,LPSI/RPSI,RPSI/LTHI,LTHI/RTHI,RTHI/LKNE,LKNE/RKNE,RKNE/LTIB,LTIB/RTIB,RTIB/LANK,LANK/RANK,RANK/LHEE,LHEE/RHEE,RHEE/LTOE,LTOE/RTOE,RTOE';
Anthropometry = 'Left_Leg_Length,800/Right_Leg_Length,800/Knee_Width,100/Ankle_Width,90/Marker_Radius,14';

static_file = matlab.net.http.io.FileProvider(["Cal 01.c3d"]); 
dynamic_file = matlab.net.http.io.FileProvider(["Walking 01.c3d"]);
formProvider = matlab.net.http.io.MultipartFormProvider("api_key",token,...
    "Marker_LBL",Markers_label,"Anthropometry",Anthropometry,"trim","50,300","Matlab","true",...
    "static_file",static_file , "dynamic_file",dynamic_file);
req = matlab.net.http.RequestMessage('post',[],formProvider);
response = req.send(uri);

if response.Body.Data.success_msg == "Done"
    IK_Result = response.Body.Data.IK_Result;
    %plot joint Kinematic 
    figure('units','normalized','outerposition',[0 0 1 1])
    subplot(2,3,1);   
    plot(IK_Result(1).angle);
    legend('Flex/Ext','Abd/Add','Ex/Int Rotation');
     title('Left Hip');

    subplot(2,3,2);   
    plot(IK_Result(2).angle);
    legend('Flex/Ext','Abd/Add','Ex/Int Rotation');
    title('Right Hip');

    subplot(2,3,3);    
    plot(IK_Result(3).angle);
    legend('Flex/Ext','Abd/Add','Ex/Int Rotation');
    title('Left Knee');

    subplot(2,3,4);   
    plot(IK_Result(4).angle);
    legend('Flex/Ext','Abd/Add','Ex/Int Rotation');
    title('Right Knee');

    subplot(2,3,5);   
    plot(IK_Result(5).angle);
    legend('Flex/Ext','Abd/Add','Ex/Int Rotation');
    title('Left Ankle');

    subplot(2,3,6);    
    plot(IK_Result(6).angle);
    legend('Flex/Ext','Abd/Add','Ex/Int Rotation');
    title('Right Ankle');

else
    disp(response.Body.Data.error_message)
end
