import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random

img = plt.imread("surface.jpeg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 1280, 0, 581])
waterx=[]
watery=[]
tunex=[]
tuney=[]
minex = []
miney = []
counter = 0
while counter<160:
    waterx.append(random.choice(range(820,870)))
    watery.append(random.choice(range(180,370)))
    tunex.append(random.choice(range(420,610)))
    tuney.append(random.choice(range(400,500)))
    minex.append(random.choice(range(550,600)))
    miney.append(random.choice(range(100,200)))
   
    counter=counter+1



plt.annotate('ESCALA 100:45 KM',xy=(1150,20),color='red',size=10)
plt.title("ORBI RED")
ax.scatter(waterx,watery,s=100,c='blue',alpha=0.3)  
ax.scatter(tunex,tuney,s=100,c='red',alpha=0.3)    
ax.scatter(minex, miney,s=100,c='purple',alpha=0.3)
plt.show()
        
