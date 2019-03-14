#coding=utf-8
import sys
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

ratio=sys.argv[1]
book=ratio[:-10]
print(book)
x=[];y1=[];y2=[]
f=open(ratio,'r')
for line in f:
    line=line.rstrip('\n')
    length,ratio,token=line.split('\t')
    length=int(length)
    ratio=float(ratio)
    token=int(token)
    x.append(length)
    y1.append(ratio)
    y2.append(token)
#print(x)
#print(y)



#plt.plot(x,y)
#plt.ylabel("token/word ratio")
#plt.xlabel("Article length (number of words)")
#plt.title("{}".format(book))
#plt.savefig(book+'.ratio.png')

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')
ax1.set_xlabel('Article length (number of words)')
ax1.set_ylabel('token/word ratio', color='g')
ax2.set_ylabel('token', color='b')
fig.set_figwidth(8)
plt.savefig(book+'.ratio.png')

