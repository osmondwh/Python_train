while True:
    num = int(input("請輸入一個整數:"))
    if num == 0:
        print("See you!")
        break
    else:     
        if num % 2 == 0:
            print("這是一個偶數")
        else:
            print("這是一個奇數")   