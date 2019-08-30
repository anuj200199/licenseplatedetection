# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 23:08:54 2019

@author: Anuj
"""
import pandas as pd
file_open=open('Indian_Number_Plates.json','r+',encoding='utf-8')
file_read=file_open.read()

seperate=file_read.split('"{""')
seperate=seperate[1:]

import re
seperate_by_des=[]
for i in seperate:
    seperate_by_des.append(re.split(',',i))
    
for i in range(0,len(seperate_by_des)):
    for j in range(0,len(seperate_by_des[i])):
        seperate_by_des[i][j]=seperate_by_des[i][j].replace('"','')
        
content=[]
label=[]
x_1=[]
y_1=[]
x_2=[]
y_2=[]

h=[]
w=[]

x_11=[]
y_11=[]
x_22=[]
y_22=[]
notes=[]
extras=[]

for i in range(0,len(seperate_by_des)):
    if(len(seperate_by_des[i])==10):
         x_11.append('')
         x_22.append('')
         y_11.append('')
         y_22.append('')
         for j in range(0,len(seperate_by_des[i])):
                if(j==0):
                     content.append(seperate_by_des[i][j].replace('content: ',''))
                if(j==1):
                    s=seperate_by_des[i][j].replace('annotation:[{label:[','')
                    label.append(s.replace(']',''))
                if(j==2):
                    notes.append(seperate_by_des[i][j].replace('notes:',''))
                if(j==3):
                    x_1.append(seperate_by_des[i][j].replace('points:[{x:',''))
                if(j==4):
                    top_left=seperate_by_des[i][j].replace('y:','')
                    y_1.append(top_left.replace('}',''))
                if(j==5):
                    x_2.append(seperate_by_des[i][j].replace('{x:',''))
                if(j==6):
                    right_bottom=seperate_by_des[i][j].replace('y:','')
                    y_2.append(right_bottom.replace('}]',''))
                if(j==7):
                    w.append(seperate_by_des[i][j].replace('imageWidth:',''))
                if(j==8):
                    height=seperate_by_des[i][j].replace('imageHeight:','')
                    h.append(height.replace('}]',''))
                if(j==9):
                    ex=seperate_by_des[i][j].replace('extras:','')
                    extras.append(seperate_by_des[i][j].replace('}',''))
    else:
        for j in range(0,len(seperate_by_des[i])):
            if(j==0):
                content.append(seperate_by_des[i][j].replace('content: ',''))
            if(j==1):
                s=seperate_by_des[i][j].replace('annotation:[{label:[','')
                label.append(s.replace(']',''))
            if(j==2):
                notes.append(seperate_by_des[i][j].replace('notes:',''))
            if(j==3):
                x_1.append(seperate_by_des[i][j].replace('points:[{x:',''))
            if(j==4):
                top_left=seperate_by_des[i][j].replace('y:','')
                y_1.append(top_left.replace('}',''))
            if(j==5):
                x_2.append(seperate_by_des[i][j].replace('{x:',''))
            if(j==6):
                right_bottom=seperate_by_des[i][j].replace('y:','')
                y_2.append(right_bottom.replace('}]',''))
            if(j==7):
                w.append(seperate_by_des[i][j].replace('imageWidth:',''))
            if(j==8):
                height=seperate_by_des[i][j].replace('imageHeight:','')
                h.append(height.replace('}',''))
            if(j==11):
                x_11.append(seperate_by_des[i][j].replace('points:[{x:',''))
            if(j==12):
                top_left=seperate_by_des[i][j].replace('y:','')
                y_11.append(top_left.replace('}',''))
            if(j==13):
                x_22.append(seperate_by_des[i][j].replace('{x:',''))
            if(j==14):
                bottom_right=seperate_by_des[i][j].replace('y:','')
                y_22.append(bottom_right.replace('}]',''))
            if(j==17):
                ex==seperate_by_des[i][j].replace('extras:','')
                extras.append(ex.replace('}',''))
                
                
content=pd.DataFrame(content)
label=pd.DataFrame(label)
x_1=pd.DataFrame(x_1)

y_1=pd.DataFrame(y_1)
x_2=pd.DataFrame(x_2)
y_2=pd.DataFrame(y_2)

h=pd.DataFrame(h)
w=pd.DataFrame(w)

x_11=pd.DataFrame(x_11)
y_11=pd.DataFrame(y_11)
x_22=pd.DataFrame(x_22)
y_22=pd.DataFrame(y_22)
notes=pd.DataFrame(notes)
extras=pd.DataFrame(extras)
                
                
dt=pd.concat((content,label,w,h,x_1,y_1,x_2,y_2,x_11,y_11,x_22,y_22,notes,extras),axis=1)         
dt.columns=(['content','label','width','height','x_1','y_1','x_2','y_2','x_11','y_11','x_22','y_22','notes','extras'])
    
dt.to_csv('indian_license_plate_csv.csv',index=False)

