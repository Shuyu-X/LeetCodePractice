"""
1、盛水容器，决定盛水多少的是短板
2、选定长板与短板，计算面积
3、用一个值存储当前计算出的面积
4、移动短板：新短板与长板计算新的面积，如果大，就更新上面的值，如果小，就保持原来的值
5、最后输出那个值就可以

为什么移动短板：因为长板不决定盛水量，盛水面积=短板*宽度，向内移动长板，短板不变宽变小，盛水量必然变小
不能排序：排序会改变顺序，导致宽度发生变化
长板怎么选：不需要指定最长的长板（无意义），使用双指针指定左右板，谁短移动谁，因为长板不参与计算，长1还是长100都没有意义。
"""

class Solution(object):
    def max(self,height):
        Left = 0
        Right = len(height) - 1 #定义左右指针，先选最远的两边
        max_area = 0 #用于记录当前面积，如果有更大的就更新，没有就保持，最后输出这个
        while Left < Right: #左右两边向中间移动，相遇后停止
            if height[Left] < height[Right]:
                area = height[Left] * (Right - Left) #计算面积，短板*宽度
                Left += 1 #左边短板，因此左边指针右移
                max_area = max(area,max_area) #比较，将更大的面积记录下来
            else: #右边板子短，则右指针左移
                area = height[Right] * (Right - Left)
                Right -= 1 #右指针左移
                max_area = max(area,max_area)
        
        return max_area

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().max(height))