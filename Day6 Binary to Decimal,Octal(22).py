b_num=list(input("input a number:"))
value=0
for i in range(len(b_num)):
    digits=b_num.pop()
    if digits=='1':
        value=value+pow(2,i)
print("the decimal value :",value) 
