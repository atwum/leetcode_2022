'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort
        nums.sort()
        output = []
        
        for i, a in enumerate(nums): #for each value in the array
            #check that the values are not repeats of previous
            if i > 0 and a == nums[i - 1]:
                continue
                
            # use two pointer method
            # a + b + c = 0
            left, right = i + 1, len(nums) - 1
        
            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1

                elif threeSum < 0:
                    left += 1 

                else: # when answer is found
                    output.append([a, nums[left], nums[right] ]) 
                    left += 1 #shift left pointer
                    #should the next one be similar, move on
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
                        
        return output
