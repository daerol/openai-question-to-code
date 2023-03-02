

def twoSum(nums, target):
    indices = list(range(len(nums)))
    map = {}
    for index, i in zip(indices, nums):
        if target - i in map:
            return [map[target-i], index]
        else:
            map[i] = index
    return []

print(twoSum([3,3], 6))

simple = [2,7,11,15]

print(twoSum(simple, 9))

simple2= [3,2,4]

print(twoSum(simple2, 6))