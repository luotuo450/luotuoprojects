import random as rd

money_list = []
money_list2 = []
money = 100
peoples = 100
for b in range(2):
    money_list1 = money_list2
    for i in range(peoples):
        get_money = round(rd.uniform(0.01, money / peoples), 2)
        money -= get_money
        money_list.append(get_money)
    money_list2 = list(map(sum, zip(money_list, money_list1)))

    print(money_list2)
max_money = max(money_list2)

# 找到最大值在列表中的位置
max_index = money_list2.index(max_money)

print(f"最大金额为{max_money}，在列表中的位置是{max_index}", max_index * 100 / peoples)
