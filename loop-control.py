#break範例
# n=0
# while n<5:
#     if n==4:
#         break
#     print(n)
#     n+=1
# print(n)
#continue範例
# n=0
# for x in  [0,1,2,3,4,5]:
#     if x%2==0:
#         continue
#     print(x)
#     n+=1
# print("最後的n是:",n)
#else 範例
sum=0
for n in range(11):
    sum=sum+n
else:
    print(sum)
#綜合實例:找出整數平方根
#輸入9得到3,輸入11得到"沒有"
n=input("輸入一個數:")
n=int(n)
for i in range(n):
    if i*i==n:
        print("整數平方根:",i)
        break
else:
    print("沒有")
