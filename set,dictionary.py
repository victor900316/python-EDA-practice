#集合的運算
s1={3,5,7}
print(3 in s1)  #in  or  not in 判斷有沒有在集合內
print(10 in s1)
s2={4,5,6,7}
s3=s1&s2 #交集:使用&符號
s4=s1|s2 #聯集:使用|符號
s5=s1-s2 #差集:從s1中,減去和s2重疊的部分
s6=s1^s2 #反交集:取兩集合中,不重疊部分
print(s3)
print(s4)
print(s5)
print(s6)
s=set("hello") #set(字串) 重疊的只會顯示一個
print(s)
#字典的運算:key-value 配對
dic={"apple":"蘋果","bug":"蟲"}
print(dic["apple"])
print("apple" in dic)
del dic["apple"] #刪除字典中的鍵值對
print(dic)
dic2={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic2)