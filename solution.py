
"""
Notes:

Pseudocode:

solution brute force:
1. loop through list
2. inside loop
  it should make sure that the index is not what the index is
  if otherwise that means you will be looking at the same index
  sum the elements
  if they are equal to the target then return the index number
 
solution hash:
1. create a dict/hash with the key as the difference and the value as the index

solution two pointers:

1. sort the list
2. create left and right index to start a end
3. if the sum is less then the target then decremt the left
4. if the sum is more then the target then increment the right
5. if its not the same index then return the solution index
6. return the values from the dict.
  

"""

class TwoPointer:
  def twoSum(self,nums,target):
    """
    time complexity: O(nlogn)
    space complexity: O(1)
    """
    #Sort the list
    nums.sort()
    #initialize the left and right pointer
    left = 0
    right = len(nums) - 1
    while left < right:
      #store the sum
      sum = nums[left] + nums[right]
      #if the sum is equal to the target then return the numbers
      if sum == target:
        return [left, right]
      #else if its less then the target then increment the left pointer
      elif sum < target:
        left += 1
      #otherwise decrese the right pointer
      else:
        right -= 1
    return []

class Hash:
  def twoSum(self, nums, target):
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    #create a dict/hash to store all the differences
    difference = {}
    #loop through list
    for i in range(len(nums)):
      #check to see if the element is in the dict
      if not nums[i] in difference:
        #if not then add it with its difference as the key
        difference[target - nums[i]] = i
      #otherwise its already there
      else:
        #just return the index number
        return [difference[nums[i]], i]
    #return an empty list
    return []

class BruteForce:
  def twoSum(self, nums, target):
    """
    time complexity: O(n^2)
    space complexity: O(1)
    """
    #loop through the whole list
    for i in range(len(nums)):
      #this will make sure that  you don't choose the same index
      for j in range(i + 1, len(nums)):
        #if the sum of the elements are equal to the target
        if nums[i] + nums[j] == target:
          #return the index numbers
          return [i, j]
    #return empty list
    return []

#Test cases
#two_pointers = TwoPointer()
#print(two_pointers.twoSum([3,2,4],6))
#print(two_pointers.twoSum([3,3],6))
#print(two_pointers.twoSum([2,7,11,15],9))

#hash = Hash()
#print(hash.twoSum([3,2,4],6))
#print(hash.twoSum([3,3],6))
#print(hash.twoSum([2,7,11,15],9))

brute_force = BruteForce()
print(brute_force.twoSum([3,2,4],6))
print(brute_force.twoSum([3,3],6))
print(brute_force.twoSum([2,7,11,15],9))