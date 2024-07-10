mark1 = int(input("write 1 subject mark :"))
mark2 = int(input("write 2 subject mark :"))
mark3 = int(input("write 3 subject mark :"))
mark4 = int(input("write 4 subject mark :"))
mark5 = int(input("write 5 subject mark :"))
mark6 = int(input("write 6 subject mark :"))

total_persentage = (100*(mark1+mark2+mark3+mark4+mark5+mark6))/600

if (total_persentage >= 60 and mark1>=33  and mark2>=33 and mark3>=33 and mark4>=33 and mark5>=33 and mark6>=33 ):
    print("you are passed ", total_persentage )
    
    
else:
    print("you r failed" ,total_persentage)


