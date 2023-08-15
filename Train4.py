order = input("歡迎使用拉麵點餐機~\n" + "(1)鹽味拉麵 $220\n" + "(2)醬油拉麵 $240\n" + "(3)豚骨拉麵 $280\n" + "請選擇拉麵口味 (輸入:1 or 2 or 3):")
enlarge = input("是否加大，豚骨口味+$50 其他口味+$30 (輸入:Y or N):").upper()
egg = input("是否加糖心蛋+$30 (輸入:Y or N):").upper()
pork = input("是否加叉燒+$60 (輸入:Y or N):").upper()

bill = 0

if order == "1":
    bill += 220
elif order == "2":
    bill += 240    
elif order == "3":
    bill +=280
if enlarge == "Y":
    if order == "3":
        bill += 50
    else:
        bill += 30
if egg == "Y":
    bill +=30

if pork == "Y": 
    bill +=60
if enlarge == "Y" and egg == "Y" and pork == "Y":
    bill -=20
    print(f"加好加滿折價$20,總金額{bill},感謝您的光臨!")
else:
    print(f"總金額{bill},謝謝您的光臨!")                   