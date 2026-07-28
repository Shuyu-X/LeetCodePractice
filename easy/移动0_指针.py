"""
移动0问题：
将非0元素前移，末尾空缺用0来填充
"""

class Solution(object):
    def __init__(self):
        self.nums = [0,1,2,0,3,4]
    def MoveZero(self):
        pos = 0 #从头开始，指定非0元素位置
        for num in self.nums:
            if num != 0:
                self.nums[pos] = num
                pos += 1
        for i in range(pos,len(self.nums)):
            self.nums[i] = 0
        return self.nums

if __name__ == "__main__":
    s = Solution()
    print(s.MoveZero())