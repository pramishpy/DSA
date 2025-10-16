def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    sMap, tMap = {}, {}
    for i in range(len(s)):
        sMap[s[i]] = sMap.get(s[i], 0) + 1
        tMap[t[i]] = tMap.get(t[i], 0) + 1
    return sMap == tMap

if __name__ == "__main__":
    print(validAnagram("anagram", "nagaram"))  # Output: True
    print(validAnagram("rat", "car"))          # Output: False
    print(validAnagram("a", "ab"))             # Output: False