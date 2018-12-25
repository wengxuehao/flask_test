# coding=utf-8
list = [1, 2, 3, 4, 5]
# 可变类型列表字典，数据对象在变化，内存地址不变化，修改或者添加id不会改变
print('列表变化之前的id:', id(list))
# 元组字符串，数值是可变类型，对象在内存的值不能变化
# 元组不能修改和删除元素
tuple = (8, 9, 10)
print('元组变化之前的id:', id(tuple))
tuple2 = (8, 9, 10, 11)
print('元组变化之后的id:', id(tuple2))
list.append(6)
# 列表添加元素之后，id不变化
print('列表变化之后的id:', id(list))
