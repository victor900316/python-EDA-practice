#有序可變動列表 List
grades=[12,60,58,90,100]
grades[0]=55 #把列表中的第一個位置換成55
print(grades)
print(grades[3])
print(grades[1:4])
grades[1:4]=[] #連續刪除列表中的資料1~4(不包括4)
grades=grades+[12,33]
print(grades)
length=len(grades)  #取得列表長度後放到新變數
print(length)
#巢狀列表
data=[[3,9,2],[6,1,8]]
print(data[0][1])
data[0][0:2]=[5,5,5] #把第一個列表中的編號0~2(不包含2),換成5,5,5
print(data[0])
#不可變動列表 Tuple
val=(3,6,9) #不可變動用小括號
val[0]=5 #錯誤:Tuple 的資料不可變動
print(val[2])