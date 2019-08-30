# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 10:01:44 2019

@author: Anuj
"""

import pandas as pd
import urllib.request

data=pd.read_csv('indian_license_plate_csv.csv')


for i in range(0,len(data)):
    urllib.request.urlretrieve(data.iloc[i][0], "images_license/image("+str(i)+").jpg")

image_name=[]
for i in range(0,len(data)):
    image_name.append('image('+str(i)+').jpg')
    
image_name=pd.DataFrame(image_name)
image_name.columns=(['image_name'])

final_data=pd.concat((data,image_name),axis=1)

final_data.to_csv('indian_license_plates_image_name.csv',index=False)
