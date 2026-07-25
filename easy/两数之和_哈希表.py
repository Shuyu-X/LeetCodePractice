class Solution(object):
#题目前提：只会有一组符合条件答案
    def __init__(self):
        self.nums = [2,11,15,7]
        self.target = 9

    def twoSum(self): #定义解决方法
        hashmap = {} #创造空哈希表

        for i,num in enumerate(self.nums): #将数组以K：V的方式展开，根据下标：i进行遍历循环
            need = self.target - num #need，目标值-当前值，要检索的值

            if need in hashmap: #检索哈希表，目标是否存在，第一轮循环为空，必然不存在
                return [hashmap[need],i] #如果存在，使用return即刻输出need的下标和当前的i
            hashmap[num] = i #如果不存在，将当前的num和i写入哈希表，用于下一轮循环检索


if __name__ == ("__main__"):
    s = Solution()

    print("开始解题")
    print(s.twoSum()) #print才会输出

    #解题思路：选择一个元素，反向寻找是否存在能够组成目标值的另一元素

    """
    定义：数组、目标
    ↓
    定义：空哈希表，笔记本，用于记录
    ↓
    以K：V形式展开列表，遍历循环
    ↓
    查询：need = target-num（目标-当前值：即期望值）
    ↓
    判断：笔记本中是否有need？
    A：有，立刻输出（因为题目前提只有一组答案）
    B：无，将当前值的kv写入笔记本，循环下一位
    """