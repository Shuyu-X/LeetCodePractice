"""
1、下标不重复
2、三元素和为0
3、对输出的元组进行去重

用于承载输出的数据结构，其构成元素应该是元组，并对此数据结构进行去重
输出的是元组，不涉及下标，所以可以对原数组的顺序进行变更
先排序：从小到大，从左开始选择三位数中的第一位
此时：第一位为数组中最小数，若＞0，则三者相加必然＞0，就没必须要继续了，直接输出null

去重的思路：不对结果去重，而是在循环过程中规避掉重复的固定数和指针数
保证每次循环的固定数，指针数都是不同的，则结果必然不会存在重复
"""
class Solution(object):
    def __init__(self):
        self.nums = [-4, -1, -1, 0, 1, 2]
    def Tirnums(self):
        result = [] #空列表用于存储结果
        print("开始解题")
        print("原始数列：",self.nums)
        self.nums.sort() #直接基于原数列调用排序方法进行排序
        print("重新排序：",self.nums)
        for i, num in enumerate(self.nums): #固定数，作为锚定结果的锚点
            if i > 0 and self.nums[i] == self.nums[i-1]: #固定数如果和前一位相同，直接跳过
                continue
            if num > 0:
                break
            else:
                left = i+1
                right = len(self.nums)-1
                while(right > left):
                    total = num + self.nums[left] + self.nums[right]
                    #left:下标，self.nums[left]:元素值
                    if total == 0: #三数和为0，符合条件，记入result 
                        #将结果作为元组写入result
                        result.append(
                            [
                            num,
                            self.nums[left],
                            self.nums[right]
                            ]
                        )
                        left += 1 #找到答案后指针同样需要移动
                        right -= 1

                        while left < right and self.nums[left] == self.nums[left-1]:
                            left += 1
                        #左指针值和前一位相同，则跳过当前，继续向右
                        while left < right and self.nums[right] == self.nums[right+1]:
                        #右指针值和前一位相同，则跳过当前，继续向左
                            right -= 1
                        #使用while循环判断，可连续跳过多个重复指针
                    elif total < 0: #总和＜0，负数大，左指针右移
                        left += 1 #左指针右移
                    else: #总和＞0，正数大，右指针左移
                        right -= 1
        print(result)
        return result

if __name__ == ("__main__"):
    s = Solution()
    s.Tirnums()