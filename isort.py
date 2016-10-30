



import random
import time
random.seed(1)
def isort(a):
    for i in range(1,len(a)):
        j = i
        beg=0
        end=i-1
        if a[j]<a[beg]:
            a.insert(0,a[j])
            del a[j+1]
        elif a[j]>a[end]:
            continue
        else:
            while (end-beg)>1:
                mid = (beg+end)//2
                if a[j]>a[mid]:
                    beg=mid
                else:
                    end=mid
            a.insert(end,a[j])
            del a[j+1]
    return a
a = []
for j in range(1,6):
    for i in range(10**j):
        a.append(random.randint(1,10**j))
    start_time=time.time()
    isort(a)
    print("--- %s seconds ---" % (time.time() - start_time))
            

