from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import svm
digits=datasets.load_digits()
import numpy as np
from PIL import Image

im = Image.open('/home/ankit/Downloads/index.png')
im = im.resize((8,8 ), Image.NEAREST)
im.save('/home/ankit/Downloads/new.png')
img = Image.open('/home/ankit/Downloads/new.png').convert('L') 
y=np.asarray(img.getdata(),dtype=np.float64).reshape((img.size[1],img.size[0]))
y=y-255
y=abs(y)
y=y/16
for i in range (0,8):
     for j in range (0,8): 
         y[i][j]="{0:0.0f}".format(y[i][j])
print(y)
y1=y.reshape(1,-1)
clf=svm.SVC(gamma=0.001,C=100)
x=digits.data[:-40]
y=digits.target[:-40]
train=clf.fit(x,y)
train=train.predict(y1)
print(train)

