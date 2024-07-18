# simple program 

number =  [1,2,3,4,5]
double_number = []
for num in number:
    double_number.append(num*2)
print(double_number)


# use list comprehension
number=[1,2,3,4,5]
list = [num*2 for num in number ]
print(list)


Empty=[]
for i in range(1,101):
    Empty.append(i)
print(Empty)

# use list comprehension
a=[i for i in range(1,101)  if i%2==0 ]
print(a)
