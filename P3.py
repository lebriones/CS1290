def count_substrings(self, s):
        n = len(s)
        count = 0
        pal = [[0]*(n) for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i]==s[j] and (j-i<2 or pal[i+1][j-1]):
                    pal[i][j] = 1
                    count+=1
        return count 