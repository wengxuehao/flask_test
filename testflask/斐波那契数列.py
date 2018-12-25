# coding=utf-8
list = []
for i in range(20):

    if i == 0 or i == 1:
        list.append(1)
    else:
        list.append(list[i-2] + list[i-1])
print(list)
