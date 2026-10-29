#儲存檔案
# file=open("data.txt",mode="w", encoding="utf-8") #開啟 若要中文要用utf-8
# file.write("hello file\n測試中文") #操作
# file.close() #關閉

# with open("data.txt",mode="w", encoding="utf-8")as file: #用with 不需要cole
#     file.write("5\n3") #操作

#讀取檔案
#把檔案中數字一行一行讀出,並計算總合
# sum=0
# with open("data.txt",mode="r", encoding="utf-8")as file:
#     for line in file:
#         sum+=int(line)
# print(sum)

#使用json格式讀取,複寫檔案
import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data) #data是一個字典資料
# print("name: ", data["name"])
# print("version: ", data["version"])
#把新資料複寫回檔案中
with open("config.json",mode="w") as file:
    json.dump(data,file) #把字典資料寫入檔案