def three_sum(nums):
    nums.sort() #把数组从小到大排序
    res = []
    n = len(nums)
    for i in range(n-2):
        if nums[i]>0:
            break

        #去掉重复的num
        if i>0 and nums[i] == nums[i-1]:
            continue

        left = i+1
        right = n-1
        while left < right:
            total = nums[i]+nums[left]+nums[right]
            if total < 0:
                left+=1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i],nums[left],nums[right]])#append只能传一个参数进去，所以传一个列表进去
                
                #去重，跳过重复的left或right
                while left < right and nums[left] == nums[left+1]:
                    left+=1
                while left < right and nums[right] == nums[right-1]:
                    right-=1
                
                #去重完毕后，双指针还要各走一步，寻找下一组在同nums[i]的情况下的可能的答案
                left+=1
                right-=1
    return res

print(three_sum([-1,0,1,2,-1,-4]))