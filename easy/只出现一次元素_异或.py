"""
异或：
相同为0，不同为1

使用0与数组中元素遍历异或：
  - a ^ a = 0（任何数异或自己等于0）
  - a ^ 0 = a（任何数异或0等于自己）

异或符合交换律：
虽然是一个一个循环异或，但数学上等价于展开数组一起异或，并且支持交换律

"""

class Solution(object):
    def __init__(self):
        self.nums = [1,1,2,2,3,3,4]
    def Onlyone(self):
        result = 0
        for i,num in enumerate(self.nums):
            result ^= num #复合运算符，result与数组元素异或并将结果赋值给result
            print(f"第{i+1}次异或，结果为：{result}") #检测每次异或运算的结果
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.Onlyone())