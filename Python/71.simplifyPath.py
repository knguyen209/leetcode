"""
https://leetcode.com/problems/simplify-path

Difficulty: Medium
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = [dir for dir in path.split('/') if dir != '' and dir != '.']

        paths = []

        i = len(arr) - 1
        
        count = 0

        while i >= 0:
            if arr[i] == '..':
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    paths.insert(0, arr[i])
            i -= 1

        return "/" + "/".join(paths)
    
print(Solution().simplifyPath("/home/"))
# /home

print(Solution().simplifyPath("/home//foo/"))
# /home/foo

print(Solution().simplifyPath("/home/user/Documents/../Pictures"))
# /home/user/Pictures

print(Solution().simplifyPath("/../"))
# /

print(Solution().simplifyPath("/.../a/../b/c/../d/./"))
# /.../b/d

print(Solution().simplifyPath("/a/./b/../../c/"))
# /c

print(Solution().simplifyPath("/a/../../b/../c//.//"))
# /c

print(Solution().simplifyPath("/home/of/foo/../../bar/../../is/./here/."))
# "/is/here"
