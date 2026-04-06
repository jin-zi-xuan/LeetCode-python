def two_sum(nums, target):
    num_dict = {}  # 记录某个数字之前是否出现过，以及它的下标

    # enumerate 可以同时取出下标 i 和当前值 num
    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_dict:
            return [num_dict[complement], i]

        # 把当前数字和它的下标存入字典
        num_dict[num] = i

    return []  # 如果没有找到，返回空列表


print(two_sum([2, 7, 11, 15], 9))