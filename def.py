#定義函式
#函式內部得程式碼,若是沒有被呼叫,就不會執行
def multiply(n1, n2):
    print(n1*n2)
    return n1*n2 #return甚麼就是什麼
#呼叫函式
value=multiply(3,4)+multiply(10,5)
print(value)

#程式的包裝
def calculate():
    sum=0
    for n in range(1,21):
        sum=sum+n
    print(sum)
    #return sum
calculate()
#value=calculate()
#print(value)