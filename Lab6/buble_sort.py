import numpy
oldlist = numpy.random.randint(0,10,8)

def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for i in range(0, last_item):
        for j in range(0, last_item - i):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    return mylist

print('Old list: ', oldlist)
newlist = bubble_sort(oldlist).copy()
print('New list: ', newlist)