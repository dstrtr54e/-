#coding:gbk
"""
程序目的：通过自定义函数，实现RPSLS游戏，即用户通过键盘输入任意一个选择（石头/剪刀/布/蜥蜴/史波克），计算机自动生成一个随机选择，根据RPSLS规则，产生最终的结果
作者：史逸驹
日期：2021年5月27日
"""

def name_to_number(name):
    if name == "石头":
        return 0
    elif name == "史波克":
        return 1
    elif name == "布":
        return 2
    elif name == "蜥蜴":
        return 3
    elif name == "剪刀":
        return 4
    else:
        print("Error: No Correct Name")
       
  
def number_to_name(number):

    if number == 0:
        return "石头"
    elif number == 1:
        return "史波克"
    elif number == 2:
        return "布"
    elif number == 3:
        return "蜥蜴"
    elif number == 4:
        return "剪刀"
    else:  
        return

import random
def rpsls(player_choice):	
    a=name_to_number(choice_name)
    b=random.randint(0,4)
    c=(a-b)%5
    print("您的选择为:",player_choice)
    print("计算机的选择为:", number_to_name(b))
    if c == 0:
        print("平局！")
    elif c == 1:
        print("你赢了!")
    elif c == 2:
        print("你赢了!")
    elif c == 3:
        print("机器赢了!")
    else:
        print("机器赢了!")


print("欢迎使用RPSLS游戏")
print("----------------")
choice_name=input("请输入您的选择:")
rpsls(choice_name)

