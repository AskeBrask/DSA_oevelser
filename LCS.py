def lcs (a, b):
    m, n = len(a), len(b)
    #intit a 2d array with zeros
    dp =[[0] * (n + 1) for _ in range(m + 1)]
         
    #build the dp array from buttom-up
    for i in range (1, m + 1):
        for j in range( 1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max (dp[i - 1][j], dp[i][j - 1])

    # the lengt of the lcs is found at dp[m][n]
    return dp[m][n]

# example of usage
a = "abcbdab"
b = "bdcab"
print("length of LCS:", lcs(a,b))

