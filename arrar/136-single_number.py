#异或：a ^ a = 0;a ^ 0 = a
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(single_number([4,1,2,1,2]))

#如果改成“出现多次”，采用通用的哈希表
def singleNumber_hash(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num,0)+1 #去字典count中找num，如果有则返回它的值，不存在默认返回0
    for num in count:
        if count[num] == 1:
            return num
print(singleNumber_hash([1,1,2]))