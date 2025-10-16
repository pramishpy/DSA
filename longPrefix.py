def longestCommon0Prefix(strs):
    if not strs:
        return""
    for str in strs:
        for i in range(len(strs[0])):
            if i == len(str) or str[i] != strs[0][i]:
                strs[0] = strs[0][:i]
                break
    return strs[0]
if __name__ == "__main__":
    print(longestCommon0Prefix(["flower","flow","flight"]))  # Output: "fl"
    print(longestCommon0Prefix(["dog","racecar","car"]))    # Output: ""