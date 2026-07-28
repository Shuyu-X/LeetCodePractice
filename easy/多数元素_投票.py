"""
最优解法为投票

我自己想出的思路是用字典
"""

class Solution(object):
    def __init__(self):
        self.nums = [5,5,5,5,5,1,1,2,2]
    def MostNumber(self):
        chosen = None #当前参与选举的候选人
        count = 0 #当前候选人持有的票数
        for i in self.nums:
            if count == 0:
                chosen = i #当目前选举人的票数归零时，退出选举，由数组中遍历到的当前元素接替参与选举
                count = 1 #自己投自己一票：计算出现次数，因此每人都有投票权
            
            elif i == chosen:
                count += 1 #遍历到的元素与自己相同，给自己投票
            else:
                count -= 1 #若不同则投反对票，抵消一票
                
        return chosen #返回活到最后的元素

if __name__ == "__main__":
    s = Solution()
    print(s.MostNumber())