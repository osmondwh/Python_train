import random
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
start = input("請輸入字母 s(剪刀) r(石頭) p(布):")

print("你出:")
if start == "s":
    print(scissor)
elif start == "r":
    print(rock)
else:
    print(paper)        
#srp = [scissor, rock, paper]

print("電腦出:")

play_two = random.randint(0,2)
if play_two == 0:
    print(scissor)
elif play_two == 1:
    print(rock)
else:
    print(paper) 

if  (start == "s" and play_two == 0) or\
    (start == "r" and play_two == 1) or\
    (start == "p" and play_two == 2):
    print("平手!!")
elif    (start == "s" and play_two == 2) or\
        (start == "r" and play_two == 0) or\
        (start == "p" and play_two == 1):
    print("恭喜你贏了")
else:
    print("你輸了 QQ")