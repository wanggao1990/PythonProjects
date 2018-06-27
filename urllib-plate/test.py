# -*- coding: utf-8 -*-

import requests
import json


folder = 'E:/PycharmProjects/urllib-plate/'
img_name = '4.jpg'

img = open(folder + img_name, 'rb')

url = 'https://api.openalpr.com/v2/recognize?recognize_vehicle=1&country=cn&secret_key=sk_DEMODEMODEMODEMODEMODEMO&return_image=true'


files = {'image': img}

multiple_files = [
        ('image', ('timg.jpg', img, 'image/jpg')),
    ]

headers = {
    'Method':'POST',
    'Referer':'http://www.openalpr.com/cloud-api.html',
    'Content-Type':'multipart/form-data',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'X-File-Name':'timg.jpg',
    'X-Requested-With':'XMLHttpRequest'
    }

params = {
          'recognize_vehicle':'1',
         'country':'cn',
          'secret_key':'sk_DEMODEMODEMODEMODEMODEMO',
          'return_image':'true'
          }

#r = requests.get(url, files = multiple_files, params = params, headers=headers )
r = requests.post(url, files = files) #, params = params, headers=headers )
r = r.json()

#file = open(folder + 'res.json','w')
#file.write(str(r))
#file.close()

#筛选结果

if not r['results']:
    exit();

res_dict = r['results'][0]
vehicle_plate    = res_dict['candidates'][0]['plate']
plate_confidence = res_dict['candidates'][0]['confidence']
plate_coordinates= res_dict['coordinates']
vehicle_color    = res_dict['vehicle']['color'][0]['name']
vehicle_region   = res_dict['vehicle_region']
vehicle_make     = res_dict['vehicle']['make'][0]['name']
vehicle_make_model=res_dict['vehicle']['make_model'][0]['name']
vehicle_body_type=res_dict['vehicle']['body_type'][0]['name']

print('vehicle_plate     :', vehicle_plate)
print('plate_confidence  : %.3f%%' % float(plate_confidence))
print('plate_coordinates :', plate_coordinates)
print('vehicle_color     :', vehicle_color)
print('vehicle_make      :', vehicle_make, vehicle_make_model)
print('vehicle_body_type :', vehicle_body_type)

#保存结果图
#import base64
#img_data = r['image_bytes'] 
#img_byte = base64.b64decode(img_data)
#with open('res_img.jpg','wb') as img:
#    img.write(img_byte)

# opencv画图
import cv2
img = cv2.imread(folder + img_name)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

plate_pts =[]
for ptDict in plate_coordinates:
    plate_pts.append((ptDict['x'],ptDict['y']))
for i in range(4):
    cv2.line(img,plate_pts[i],plate_pts[(i+1)%4], (0,0,255),4)
    
car_rect_tl = (vehicle_region['x'],vehicle_region['y'])
car_rect_br = (vehicle_region['x'] + vehicle_region['width'], vehicle_region['y']+vehicle_region['height'])
cv2.rectangle(img, car_rect_tl, car_rect_br, (0,255,0),2)

#cv2.putText(img, vehicle_plate, car_rect_br, 1, 1, (0,255,0), 2)    

import numpy
from PIL import Image, ImageDraw, ImageFont

def new_pt(pt,off):
    return (pt[0]+off[0],pt[1]+off[1])

img_PIL = Image.fromarray(img)
draw = ImageDraw.Draw(img_PIL)

ft_size = 20
tf_color = (255,0,0)
ft = ImageFont.truetype("C:/Windows/Fonts/SIMYOU.TTF", ft_size)

draw.text(car_rect_tl, vehicle_plate, font=ft, fill= tf_color)
draw.text(new_pt(car_rect_tl,(0,ft_size)), str(plate_confidence), font=ft, fill=tf_color) 
draw.text(new_pt(car_rect_tl,(0,ft_size*2)), vehicle_color, font=ft, fill= tf_color)
draw.text(new_pt(car_rect_tl,(0,ft_size*3)), vehicle_body_type, font=ft, fill= tf_color)
draw.text(new_pt(car_rect_tl,(0,ft_size*4)), vehicle_make+" "+vehicle_make_model,font=ft,fill=tf_color)


img = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)

cv2.namedWindow('img',0)
cv2.imshow('img',img )
cv2.waitKey(0)
