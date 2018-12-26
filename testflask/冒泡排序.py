# coding=utf-8
def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums) - i - 1):  # j为列表下标
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# print(bubble_sort([45, 32, 8, 33, 12, 22, 19, 97]))
# 输出：[8, 12, 19, 22, 32, 33, 45, 97]


# 冒泡排序
list = [45, 32, 8, 33, 12, 22, 19, 97]
print(len(list))
# 遍历数组中的数字
for i in range(len(list) - 1):
    # 比较当前数字和后一个数字的差别
    for j in range(len(list) - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

# print(list)
