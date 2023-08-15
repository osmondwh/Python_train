while True:
    height = float(input("請輸入你的身高(公分):"))
    kilogram = float(input("請輸入你的體重(公斤):"))
    if height == 0.0:
        print("結束")
        break
    else:
        bmi = round(kilogram / (height / 100)**2 ,1)
        if bmi <18.5 :
            print(f"您的BMI為{bmi}(體重過輕)")
        elif    bmi <24:
            print(f"您的BMI為{bmi}(正常體位)")
        elif    bmi <27:
            print(f"您的BMI為{bmi}(體重過重)")
        elif    bmi <30:
            print(f"您的BMI為{bmi}(輕度肥胖)")
        elif    bmi <35:
            print(f"您的BMI為{bmi}(中度肥胖)")
        else:                
            print(f"您的BMI為{bmi}(重度肥胖)")