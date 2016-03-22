import time
x = 0
def doit1(i):
    global x
    x = x + i

list = range(100000)
t = time.time()
for i in list:
    doit1(i)
f=time.time()
print ("%.3f" % (f-t))
