def levenshtein(string1, string2):
    dp = [[0]*(len(string1)+1) for _ in range(2)]

    dp[0] = list(range(len(string1) + 1))

    for i in range(1,len(string2)):
        for j in range(len(string1)):
            aux = not i&1
            if not j:
                dp[aux][j] = i

            elif string1[j - 1] == string2[i - 1]:
                dp[aux][j] = dp[not aux][j-1]
            
            else:
                dp[aux] = 1 + min(dp[not aux][j],
                                  dp[aux][j-1],
                                  dp[not aux][j-1])
    
    return dp[not len(string2) & 1][len(string1)]