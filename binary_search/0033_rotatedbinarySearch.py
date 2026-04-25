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
            if nums[left] <= target < nums[mid]:
                right = mid-1 #target在左边，去左边找
            else:
                left = mid + 1 #target在右边，去右边找
            
        else:
            # === 右半边是完美有序的 ===
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
            
    return -1

print(rotatedbinarySearch([4, 5, 6, 7, 0, 1, 2],0))