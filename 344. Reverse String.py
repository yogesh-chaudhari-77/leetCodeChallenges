class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) == 0:
            return ''
        elif len(s) == 1:
            return s

        i = 0;
        j = len(s) - 1

        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1

        return s


s = Solution()
print(s.reverseString(["a", "b", "c", "d"]))
