def find_max(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return(num1)
    elif num2 >= num1 and num2 >= num3:
        return(num2)
    else:
        return(num3)   

def find_min(num1,num2,num3):
    if num1 <= num2 and num1 <= num3:
        return(num1)
    elif num2 <= num1 and num2 <= num3:
        return(num2)
    else:
        return(num3)  
def max_min(num1,num2,num3):
    if type(num1) != int or type(num2) != int or type(num3) != int:
        return("請輸入整數")
    else:
        return find_max(num1,num2,num3) - find_min(num1,num2,num3)

num = max_min(1,20,99)
print(num)