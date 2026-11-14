class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        Map = {} 
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if (Map.get(char_s) == None):
                Map[char_s] = 1
            else:
                Map[char_s] += 1
            if (Map.get(char_t) == None): 
                Map[char_t] = -1
            else:
                Map[char_t] -= 1
        return all(v == 0 for v in Map.values())
        
            
