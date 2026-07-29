"""
set(): 哈希表的另一种实现，无重复元素，只存值，非键值对

本题求最长连续序列，可先用set()转化为集合，方便匹配并且可以去重
"""

class Solution(object):
    def Longest(self,nums):
        nums_set = set(nums) #将数组元素存入set哈希表中，并去重
        longest = 0 #记录最长连续序列的长度
        for num in nums_set: 
            if num - 1 in nums_set:
                continue # 当前数字前一位在数组中也存在，说明不是最小，跳过
            else:
                current_num = num
                current_length = 1 #记录长度，用于最后输出
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1
                longest = max(longest, current_length)
                # 如果当前长度大于记录的最长长度，则更新
        return longest

if __name__ == "__main__":
    nums = [100,400,1,2,5,3,4]
    print(Solution().Longest(nums))
