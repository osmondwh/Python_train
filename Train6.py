def get_bmi(height,weight):
    return round(weight / (height / 100) **2,1)
def get_bmr(sex,height,weight,age):
    if sex == "男":
        bmr = 66 + (13.7 * weight + 5 * height - 6.8 * age)
    else:
        bmr = 655 + (9.6 * weight + 1.8 * height - 4.7 * age)
    bmr = round(bmr,2)
    return bmr
def get_tdee(sex,height,weight,age,times):
    bmr = get_bmr(sex,height,weight,age)
    tdee = bmr * times
    tdee = round(tdee,2)
    return tdee
print("歡迎使用綜合計算機~")
print("(1)計算BMI")
print("(2)計算基礎代謝率(BMR)")
print("(3)計算總熱量消耗(TDEE)")
choose = input("請選擇要計算的項目(輸入1 or 2 or3):")
if choose == "1":
    height = float(input("請輸入您的身高(公分):"))
    weight = float(input("請輸入你的體重(公斤):"))
    bmi = get_bmi(height,weight)
    print(f"您的BMI為:{bmi}")
elif choose == "2":
    sex = input("請輸入您的性別(男or女):")
    height = float(input("請輸入您的身高(公分):"))
    weight = float(input("請輸入你的體重(公斤):"))
    age = int(input("請輸入您的年紀:"))
    bmr = get_bmr(sex,height,weight,age)
    print(f"您的基礎代謝率(BMR):{bmr}")
elif choose == "3":
    sex = input("請輸入您的性別(男or女):")
    height = float(input("請輸入您的身高(公分):"))
    weight = float(input("請輸入你的體重(公斤):"))
    age = int(input("請輸入您的年紀:"))
    print("(1)久坐、幾乎沒運動")
    print("(2)每週低強度運動1~3天")
    print("(3)每週中強度運動3~5天")
    print("(4)每週高強度運動6~7天")
    print("(5)勞力密集工作或是每天高強度訓練")
    exer = input("請選擇您的運動量(輸入1~5):")
    times = 0
    if exer == "1":
        times = 1.2
    elif exer == "2":
        times = 1.375
    elif exer == "3":
        times = 1.55
    elif exer == "4":
        times = 1.725
    elif exer == "5":
        times = 1.9
    tdee = get_tdee(sex,height,weight,age,times)
    print(f"您的總熱量消耗(TDEE):{tdee}")