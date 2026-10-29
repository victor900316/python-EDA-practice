#判斷式
x=input("請輸入數字:") #以字串形式取得輸入
x=int(x) #將字串轉換成數字型態
if x>100:
    print("x大於100")
elif x>50:
    print("x大於50,小於等於100")
else:
    print("x小於等於50")

#四則運算
n1=int(input("請輸入數字1:"))
n2=int(input("請輸入數字2:"))
op=input("請輸入運算:+,-,*,/ :")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("error")