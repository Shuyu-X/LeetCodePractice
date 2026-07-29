"""
将单词按字母顺序重排序
然后存入字典进行哈希匹配

字典中存储的数据接口：
key：单词重排序后的字母   eg: "eat" → "aet" ,"tea" → "aet"
value：符合上述条件的所有单词构成的列表   eg："aet"：["eat","tea"] 

算法逻辑：
遍历原词组，选取一个单词
按字母表顺序重排为key：
↓
哈希匹配：
若字典中存在该key，则：将当前单词存入该key对应的value列表中
若字典中不存在该key，则：字典中新增一个key，并将该单子写入对应的列表中
↓
输出：输出该字典，就是以key为维度的多个列表

  图解流程：["eat","tea","tan","ate","nat","bat"]

  遍历每个字符串：
    "eat" → key="aet" → groups: {"aet": ["eat"]}
    "tea" → key="aet" → groups: {"aet": ["eat", "tea"]}
    "tan" → key="ant" → groups: {"aet": ["eat","tea"], "ant": ["tan"]}
    "ate" → key="aet" → groups: {"aet": ["eat","tea","ate"], "ant": ["tan"]}
    "nat" → key="ant" → groups: {"aet": ["eat","tea","ate"], "ant": ["tan","nat"]}
    "bat" → key="abt" → groups: {"aet": ["eat","tea","ate"], "ant": ["tan","nat"], "abt": ["bat"]}

  结果：[["eat","tea","ate"], ["tan","nat"], ["bat"]] ✅
"""

class Solution(object):
    def groupAnagrams(self,words):
        result = {} #创建一个空字典存储结果
        for word in words: #遍历词组每个单词
            key = ''.join(sorted(word))  
            #sorted(word)：拆解单子，并重排序   .join():将拆解的字母重新拼回单词   ''：分隔符，为空表示拼接时不分割，若内容为'-',单词为"eat",则拼接后为"a-e-t"
            
            if key in result: #如果字典中是否有该key值
                result[key].append(word) #将当前单词存入key对应的列表中
            else:
                result[key] = [word] #否则以当前key创建新的列表，并将单词存入
        
        return list(result.values()) #将字典中作为value存在的列表返回出来

if __name__ == "__main__":
    words = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(words))
