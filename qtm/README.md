# Qualisys Scripting : C3Dtools
If you are a QTM user, you can use this script to convert your c3d files to trc and mot files that are compatible with OpenSim

# Installation
## step 1:
Download the **install_package.bat** and **qtm_C3Dtools.py** from this repository, then run the batch file to install the Python packages that you need.

## step 2:
Open your QTM project and open the **project options window > Miscellaneous > Scripting**. Then add the **qtm_C3Dtools.py** to Script files by clicking on the Add button.
Now, you can see the C3Dtools option on the QTM menu.

# Usage
Open your QTM project and then export your C3D files to the same folder (the folder in which the .qtm files are stored).
Next, from the menu click on **C3Dtools > C3D to Opensim**. Now you can see messages in the Messages box. According to the file size it might take a while because this script uses C3Dtools API and your files will process via C3Dtools web-based services. Finally, you can find the trc and mot files besides the .qtm files.


![qtm scripting](https://github.com/etoshey/pyc3dtools/blob/707bf76feae23ac27ba6fec91db65fa4e84df0ca/Test/Capture.JPG)
