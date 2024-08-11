def insertionsort(list1):
    for i in range(1, len(list1)):
        temp=list1[i]
    
        j=i-1
        while j>=0 and temp<list1[j]:
           list1[j+1]=list1[j]
           j-=1
        list1[j+1]=temp
           
mylist=[11,21,22,123,32,34]
insertionsort(mylist)
print(mylist)

#ex3pense_share#
