# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:58:00 2019

@author: Anuj
"""
import pandas as pd
data=pd.read_csv('bounding_box_values.csv')

def convert(width,height,x1,x2,y1,y2):
    dw=1./width
    dh=1./height
    x=(x1+x2)/2.0
    y=(y1+y2)/2.0
    w=x2-x1
    h=y2-y1
    x=x*dw
    w=w*dw
    y=y*dh
    h=h*dh
    return (x,y,h,w)


for i in range(0,len(data)):
    file=open('text/image('+str(i)+').txt','w')
    file.close()
    


for i in range(0,len(data)):
    x,y,h,w=convert(data.iloc[i]['width'],data.iloc[i]['height'],data.iloc[i]['x_top_left'],data.iloc[i]['x_bottom_right'],data.iloc[i]['y_top_left'],data.iloc[i]['y_bottom_right'])
    file=open('text/image('+str(i)+').txt','r+')
    file.write('0'+' ')
    file.write(str(x)+' ')
    file.write(str(y)+' ')
    file.write(str(w)+' ')
    file.write(str(h)+' ')
    
    file.close()
    

for i in range(0,len(data)):
    if(data.iloc[i]['x1_top_left']!=0):
        print(i)
        x,y,h,w=convert(data.iloc[i]['width'],data.iloc[i]['height'],data.iloc[i]['x1_top_left'],data.iloc[i]['x1_bottom_right'],data.iloc[i]['y1_top_left'],data.iloc[i]['y1_bottom_right'])
        file=open('text/image('+str(i)+').txt','a+')
        file.write('\n0'+' ')
        file.write(str(x)+' ')
        file.write(str(y)+' ')
        file.write(str(w)+' ')
        file.write(str(h)+' ')
        
        file.close()
    