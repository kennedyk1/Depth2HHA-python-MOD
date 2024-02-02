import cv2
import os
from getHHA import *

input_folder = '/home/kmota/dataset/inhouse/DEEC/depth/images'
output_folder = '/home/kmota/dataset/inhouse/DEEC/HHA/images'

files = os.listdir(input_folder)

try:
    os.makedirs(output_folder)
except:
    pass


for i in range(len(files)):
    print(i,'/',len(files),'-',files[i])
    D = cv2.imread(os.path.join(input_folder,files[i]), cv2.COLOR_BGR2GRAY)/65535.0
    D= -80.0/(D*79.0-80.0); 
    camera_matrix = getCameraParam('color')
    hha = getHHA(camera_matrix, D, D)
    cv2.imwrite(os.path.join(output_folder,files[i]),hha)


input_folder = '/home/kmota/dataset/inhouse/DEI/depth/images'
output_folder = '/home/kmota/dataset/inhouse/DEI/HHA/images'

files = os.listdir(input_folder)

try:
    os.makedirs(output_folder)
except:
    pass


for i in range(len(files)):
    print(i,'/',len(files),'-',files[i])
    D = cv2.imread(os.path.join(input_folder,files[i]), cv2.COLOR_BGR2GRAY)/65535.0
    D= -80.0/(D*79.0-80.0); 
    camera_matrix = getCameraParam('color')
    hha = getHHA(camera_matrix, D, D)
    cv2.imwrite(os.path.join(output_folder,files[i]),hha)
