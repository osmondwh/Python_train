i = int(input("請輸入要算的數字:"))
s = i
num = 0
while i > 0:
    num = num + i
    i -= 1
print(f"你輸入的是{s}結果是{num}")