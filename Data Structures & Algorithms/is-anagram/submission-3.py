class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_s = {}
        check_t = {}
        for i in range(len(s)):
            if s[i] not in check_s:
                check_s[s[i]] = 1
            else:
                check_s[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in check_t:
                check_t[t[j]] = 1
            else:
                check_t[t[j]] += 1
        if check_s == check_t:
            return True
        else:
            return False
