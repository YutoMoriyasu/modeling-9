from google.colab import files

f = open('data4.csv','w')

list1=[[ [] for i in range(101)] for j in range(1001)]
for i in range(101):
        list1[0][i]=300.0
list1[0][50]=500.0

dx=1.0
dt=0.1
alpha=1.0
u=0.2
c1=(alpha*dt)/(dx*dx)
c2=(u*dt)/(2*dx)

for istep in range(0,1000):
        if istep%100==0:
                print('step = '+str(istep))
        for i in range(1,100):
                list1[istep+1][i] = list1[istep][i] - c2 * (list1[istep][i+1] - list1[istep][i-1]) + c1*(list1[istep][i+1] - list1[istep][i] * 2.0 + list1[istep][i-1])
        list1[istep+1][0]=300.0
        list1[istep+1][100]=300.0

for i in range(101):
        f.write(str(i)+',')
        for istep in range(1,1001):
                if istep%100==0:
                        f.write(str(list1[istep][i])+',')
        f.write('\n')

f.close()

files.download("data4.csv")
