class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        triplets = []
        nums.sort()
        while i < len(nums):
            j = i+1
            k = len(nums) - 1


            while j < k:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    if [nums[i], nums[j], nums[k]] not in triplets:
                        triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                
                elif (nums[i] + nums[j] + nums[k]) < 0:
                    j += 1
                    continue
                
                else:
                    k -= 1
                    continue


            i += 1

        return triplets
        