#隨機點餐系統
import random
print("歡迎使用今晚吃甚麼~")
food_str = input("請輸入晚餐的選項(中間請使用,隔開)\n")
food_list = food_str.split(",")
tonight_food =food_list[random.randint(0,len(food_list)-1)]
print(f"今晚吃  {tonight_food}!")

#dinner = ["拉麵","滷肉飯","鱔魚意麵","火鍋"]
#today_dinner = dinner[random.randint(0,len(dinner)-1)]
#print(f"今晚吃  {len(dinner)-1}")