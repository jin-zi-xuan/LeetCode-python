def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num-1 not in num_set: #如果num-1不在集合里，说明num是连续序列的第一个数
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num+=1
                current_length+=1

            longest = max(longest,current_length)
    return longest

print(longestConsecutive([100,4,200,1,2,3]))