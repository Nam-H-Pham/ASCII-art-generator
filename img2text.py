# -*- coding: utf-8 -*-
import cv2
from PIL import Image

path = ('leaf.jpg')

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.imwrite("gray.png", img)
img = cv2.imread('gray.png',1)

height, width, channels = img.shape


#while height > 50 or width > 50:
#  height, width, channels = img.shape
#  img = cv2.resize(img,None,fx=0.9,fy=0.9,interpolation=cv2.INTER_CUBIC)

img2 = img.copy()

shades = ("#%$&whio:,._-")
sl = []
for i in shades:
          sl.append(i)

multiplier = 255/len(shades)


text = "```"
text += "\n"

for y in xrange(img.shape[0]):
  for x in xrange(img.shape[1]):
        brightness = sum([img[y,x,0],img[y,x,1],img[y,x,2]])/3
        text_before = text
        for unit in shades:
          #print unit,(shades.index(unit)*multiplier,shades.index(unit)*multiplier+ multiplier)
          if brightness in range(shades.index(unit)*multiplier,shades.index(unit)*multiplier+ multiplier):
            text += shades[int(shades.index(unit))]
            break
        if text_before == text:
          text += ' '
  text += "\n"
  
text += "```"

print (text.decode('utf-8'))

RAW = open(path+".txt" ,"w")      
RAW.write(text)
RAW.close()


