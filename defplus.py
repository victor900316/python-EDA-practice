#參數的預設資料
def power(base,exp=0):
    print(base**exp)
power(3,2)
power(9) #沒給第二個參數所以會錯誤,所以改exp=0,這樣沒給預設的話就會給定0
#使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=2,n1=4)
#無限/不定 參數資料
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))
avg(3,4)
avg(2,5,9)