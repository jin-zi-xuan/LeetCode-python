def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
            #原地哈希：（交换代码） 把数字x放到x-1的位置
            #for...while会一直交换到所有的数归位
            temp = nums[i]#先把当前位置原来的数保存到temp
            nums[i] = nums[temp-1]#把目标位置上的数拿回当前位置
            nums[temp-1] =temp#再把原来的那个书放到它该去的位置

    for i in range(n):
            if nums[i] != i+1:
                #一旦找到位置不对的数字，立刻return然后结束整个函数
                return i+1
    return n+1
print(firstMissingPositive([1,2,0]))

#假设用set 但此题不符合条件
def firstMissing_set(nums):
     num_set = set(nums)
     target = 1

     while target in num_set:
          target += 1
     return target

print(firstMissing_set([1,2,0]))