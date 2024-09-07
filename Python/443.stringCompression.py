from typing import List

"""
https://leetcode.com/problems/string-compression

Difficult: Medium
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        read_ptr = 1
        write_ptr = 1
        count = 1

        while read_ptr < len(chars):
            if chars[read_ptr] == chars[read_ptr - 1]:
                count += 1
            else:
                if count > 1:
                    for c in str(count):
                        chars[write_ptr] = c
                        write_ptr += 1
                chars[write_ptr] = chars[read_ptr]
                write_ptr += 1
                count = 1

            read_ptr += 1
        
        # print(chars)
        # print(read_ptr, write_ptr, count)
        
        if count > 1:
            chars[write_ptr] = chars[read_ptr - 1]
            
            for c in str(count):
                chars[write_ptr] = c
                write_ptr += 1
        # print(write_ptr)

        # print(chars)

        return write_ptr
    
chars = ["a","a","b","b","c","c","c"]
print(Solution().compress(chars))

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(Solution().compress(chars))

# chars = ["a"]
# print(Solution().compress(chars))

# chars = ["a","a","b","b","c","c","c"]
# print(Solution().compress(chars))
