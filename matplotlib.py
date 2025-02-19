import numpy as np #x=[min,max]
import matplotlib.pyplot as plt

x1=np.arange(0,10,1)
y1=(2/27)*x1**2-3

x2=np.arange(-10,0.5,0.5) #min,max+step,step
y2=0.004*x2**2-3

x3=np.arange(-9,-2.5,0.5)
y3=(2/9)*(x3+6)**2+1

x4=np.arange(-3,9.5,0.5)
y4=(-1/12)*(x4-3)**2+6

x5=np.arange(5,9,0.5)
y5=(1/9)*(x5-5)**2+2

x6=np.arange(5,8.5,0.5)
y6=(1/8)*(x6-7)**2+1.5

x7=np.arange(-13,-8.5,0.5)
y7=(-0.75)*(x7+11)**2+6

x8=np.arange(-15,-12.5,0.5)
y8=(-0.5)*(x8+13)**2+3

x9=np.arange(-15,-10,0.5)
y9=[1]*len(x9)

x10=np.arange(3,4,0.5)
y10=[3]*len(x10)

plt.figure(facecolor="lightpink")
plt.title("Vaal")
plt.ylabel("Y")
plt.xlabel("X")
plt.grid(True)
ax=plt.axes()
ax.set_facecolor("lightblue")
#plt.plot(x1,y1,"r:o")
colors=["c","m","y","r","g","b","w","k","k","k"]
for i in range(1,11):
    plt.plot(eval(f"x{i}"),eval(f"y{i}"),colors[i-1]+"-*")#eval(f"{colors[i-1]}-*")) #"b-*" цвет, стиль линии и маркер
plt.show()