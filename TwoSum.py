#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        locations = {}
        for i in range(len(nums)):
            num = nums[i]
            match = target - num
            if locations.get(num) == None :  # if the latest item isn't in the hashmap we add it
                locations[num] = i  # now all unique numbers should be in the locations
            # then check to see if the match is in there
            if match in locations:  # if the target number is in the hashmap, then it will return a number
                if locations[match] != i: #dont choose the same index twice
                    return [i,locations[match]]