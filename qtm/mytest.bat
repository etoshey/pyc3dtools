@echo off

if _%1_==_payload_  goto :payload

:getadmin
    echo %~nx0: elevating self
    set vbs=%temp%\getadmin.vbs
    echo Set UAC = CreateObject^("Shell.Application"^)                >> "%vbs%"
    echo UAC.ShellExecute "%~s0", "payload %~sdp0 %*", "", "runas", 1 >> "%vbs%"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
goto :eof



:payload
echo Step1 : Setup pyc3dtools package on QTM
set python=\python.exe
set qtm_Path=C:\Program Files (x86)\Qualisys\Qualisys Track Manager


:filecheck
set qtm_python=%qtm_Path%%python%
IF EXIST "%qtm_python%" (
echo QTM is found...
) else (
set /p qtm_Path= Enter the QTM directory path:
goto filecheck
)




echo Step 2 : Python Package Installation
rem python package installation
cd %qtm_Path%
rem python -m pip list
python -m pip install pyc3dtools
pause