class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # 法1.循环s 480ms
#         res = []
#         if not s or not words:
#             return res
#         words_hash = {}
#         word_len = len(words[0])
#         words_len = len(words)
#         s_len = len(s)
        
#         for word in words:
#             words_hash[word] = words_hash.get(word, 0) + 1
        
#         for i in range(0, s_len - words_len * word_len + 1):
#             cur_hash = {}
#             j = 0
#             while j < words_len:
#                 cur_word = s[i + j * word_len : i + (j + 1) * word_len ]
#                 if not words_hash.get(cur_word, 0):
#                     break
#                 cur_hash[cur_word] = cur_hash.get(cur_word, 0) + 1
#                 if cur_hash[cur_word] > words_hash[cur_word]:
#                     break
#                 j += 1
#             if j == words_len:
#                 res.append(i)
#         return res
    
        # 法2.循环len(word[0])  44ms
        ans = []
        if not s or not words:
            return ans
        
        words_hash = {}
        word_len = len(words[0])
        words_len = len(words)
        s_len = len(s)
        
        for word in words:
            words_hash[word] = words_hash.get(word, 0) + 1
            
        for k in range(word_len):
            left = k
            cur_hash = {}
            count = 0
            for j in xrange(k, s_len - word_len + 1, word_len):
                tword = s[j:j+word_len]
                # valid word
                if tword in words_hash:
                    if tword in cur_hash:
                        cur_hash[tword] += 1
                    else:
                        cur_hash[tword] = 1
                    count += 1
                    while cur_hash[tword] > words_hash[tword]:
                        cur_hash[s[left:left+word_len]] -= 1
                        left += word_len
                        count -= 1
                    if count == words_len:
                        ans.append(left)
                # not valid
                else:
                    left = j + word_len
                    cur_hash = {}
                    count = 0
        return ans


