#coding:gbk
"""
����Ŀ�ģ�ͨ���Զ��庯����ʵ��RPSLS��Ϸ�����û�ͨ��������������һ��ѡ��ʯͷ/����/��/����/ʷ���ˣ���������Զ�����һ�����ѡ�񣬸���RPSLS���򣬲������յĽ��
���ߣ�ʷ�ݾ�
���ڣ�2021��5��27��
"""

def name_to_number(name):
    if name == "ʯͷ":
        return 0
    elif name == "ʷ����":
        return 1
    elif name == "��":
        return 2
    elif name == "����":
        return 3
    elif name == "����":
        return 4
    else:
        print("Error: No Correct Name")
       
  
def number_to_name(number):

    if number == 0:
        return "ʯͷ"
    elif number == 1:
        return "ʷ����"
    elif number == 2:
        return "��"
    elif number == 3:
        return "����"
    elif number == 4:
        return "����"
    else:  
        return

import random
def rpsls(player_choice):	
    a=name_to_number(choice_name)
    b=random.randint(0,4)
    c=(a-b)%5
    print("����ѡ��Ϊ:",player_choice)
    print("�������ѡ��Ϊ:", number_to_name(b))
    if c == 0:
        print("ƽ�֣�")
    elif c == 1:
        print("��Ӯ��!")
    elif c == 2:
        print("��Ӯ��!")
    elif c == 3:
        print("����Ӯ��!")
    else:
        print("����Ӯ��!")


print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
choice_name=input("����������ѡ��:")
rpsls(choice_name)

