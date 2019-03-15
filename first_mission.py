import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
rng=np.random.RandomState(0)
color=rng.rand(502)
yaxis=np.random.normal(1,100,502)
xaxis=[i for i in range(0,len(yaxis))]
pos=np.arange(len(yaxis))+0.01
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
i=0
def quicksho(arr):
    global i,yaxis
    i=i+1
    key=yaxis[i]
    j=i-1
    while j>=0 and yaxis[j]>key and i<len(yaxis):
        yaxis[j+1]=yaxis[j]
        j=j-1
    yaxis[j+1]=key
    ax1.clear()
    plt.scatter(pos,yaxis,c=color)
    print(yaxis)
ani=animation.FuncAnimation(fig,quicksho,interval=10)
plt.show()
print(yaxis)























