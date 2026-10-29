#載入內建的sys模組並取得資訊
# import sys
# print(sys.platform)
# print(sys.maxsize)
# #建立 geometry 模組,載入使用
# import modules.geometry as geometry
# result=geometry.distance(2,2,4,4)
# print(result)

#調整搜尋模組的路徑
import sys
sys.path.append("modules")
print(sys.path)
print("-------------------")
import geometry
print(geometry.distance(2,2,4,4))