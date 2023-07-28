num1=float(input("enter the first number= "))
op=input("enter the operation= ")
num3=float(input("enter the third number= "))



if op=="+":
    print(str(num1)+"+"+str(num3)+"="+str(num1+num3))
elif op=="-":
    print(str(num1)+"-"+str(num3)+"="+str(num1-num3))
elif op=="*":    
    print(str(num1)+"*"+str(num3)+"="+str(num1*num3))
elif op=="/":
     print(str(num1)+"/"+str(num3)+"="+str(num1/num3))
else:
    print("get lost ")      

