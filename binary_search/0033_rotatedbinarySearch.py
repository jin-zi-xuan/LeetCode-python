def rotatedbinarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
            
        # 判断哪一半是完美有序的
        if nums[left] <= nums[mid]:
            # === 左半边是完美有序的 ===
            # 【你的任务：在这里写代码】
            # 提示：判断 target 是不是在 nums[left] 到 nums[mid] 之间？
            # 如果在，移动 right；如果不在，移动 left。
            
        else:
            # === 右半边是完美有序的 ===
            # 【你的任务：在这里写代码】
            # 提示：判断 target 是不是在 nums[mid] 到 nums[right] 之间？
            # 如果在，移动 left；如果不在，移动 right。
            
    return -1
    print(rotatedbinarySearch([4, 5, 6, 7, 0, 1, 2],0))