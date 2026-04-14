def searchRange(nums, target):
    # 辅助函数 1：寻找左边界
    def get_left_border(nums, target):
        left, right = 0, len(nums) - 1
        left_border = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:  # 注意这里的 >= 
                right = mid - 1      # 只要大于等于，右边界就疯狂往左压，试图找到最左边的 target
                if nums[mid] == target:
                    left_border = mid # 记下当前的候选位置
            else:
                left = mid + 1
        return left_border

    # 辅助函数 2：寻找右边界
    def get_right_border(nums, target):
        left, right = 0, len(nums) - 1
        right_border = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:  # 注意这里的 <=
                left = mid + 1       # 只要小于等于，左边界就疯狂往右压，试图找到最右边的 target
                if nums[mid] == target:
                    right_border = mid # 记下当前的候选位置
            else:
                right = mid - 1
        return right_border

    # 主逻辑：跑两次二分，搞定！
    left_idx = get_left_border(nums, target)
    right_idx = get_right_border(nums, target)
    
    return [left_idx, right_idx]

print(searchRange([5,7,7,8,8,10],8))