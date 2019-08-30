# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 10:13:50 2019

@author: Anuj
"""

import pandas as pd
import cv2

datas=pd.read_csv('indian_license_plates_image_name.csv')


x_top_left=[]
x_bottom_right=[]
y_top_left=[]
y_bottom_right=[]

x1_top_left=[]
x1_bottom_right=[]
y1_top_left=[]
y1_bottom_right=[]

data=datas.fillna(0)
for i in range(0,len(data)):
    
    image_name=data.iloc[i]['image_name']

    x1=data.iloc[i]['x_1']
    y1=data.iloc[i]['y_1']
    x2=data.iloc[i]['x_2']
    y2=data.iloc[i]['y_2']

    x11=data.iloc[i]['x_11']
    y11=data.iloc[i]['y_11']
    x22=data.iloc[i]['x_22']
    y22=data.iloc[i]['y_22']
    
    w=float(data.iloc[i]['width'])
    h=float(data.iloc[i]['height'])

    x_1=int(x1*w)
    y_1=int(y1*h)
    x_2=int(x2*w)
    y_2=int(y2*h)
    
    x_11=int(x11*w)
    y_11=int(y11*h)
    x_22=int(x22*w)
    y_22=int(y22*h)
    
    
    x_top_left.append(x_1)
    x_bottom_right.append(x_2)
    y_top_left.append(y_1)
    y_bottom_right.append(y_2)
    
    
    x1_top_left.append(x_11)
    x1_bottom_right.append(x_22)
    y1_top_left.append(y_11)
    y1_bottom_right.append(y_22)
    
    
x_top_left=pd.DataFrame(x_top_left)

x_bottom_right=pd.DataFrame(x_bottom_right)

y_top_left=pd.DataFrame(y_top_left)

y_bottom_right=pd.DataFrame(y_bottom_right)

x1_top_left=pd.DataFrame(x1_top_left)

x1_bottom_right=pd.DataFrame(x1_bottom_right)

y1_top_left=pd.DataFrame(y1_top_left)

y1_bottom_right=pd.DataFrame(y1_bottom_right)

original_dimensions_of_box=pd.concat((x_top_left,y_top_left,x_bottom_right,y_bottom_right,x1_top_left,y1_top_left,x1_bottom_right,y1_bottom_right),axis=1)
original_dimensions_of_box.columns=(['x_top_left','y_top_left','x_bottom_right','y_bottom_right','x1_top_left','y1_top_left','x1_bottom_right','y1_bottom_right'])

final_data=pd.concat((datas,original_dimensions_of_box),axis=1)
final_data.to_csv('bounding_box_values.csv')


