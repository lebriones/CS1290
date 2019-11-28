def min_path(A):
    for row in A:
        for col in A[row]:
            if col == 0: #first row, only check top and right
                A[row][col] += min(A[row-1][col], A[row-1][col+1])
            if col == len(A)-1: #last row, only check top and left
                A[row][col] += min(A[row-1][col], A[row-1][col-1])
            #row somewhere in middle, check all 3 options
            A[row][col] += min(A[row-1][col], A[row-1][col-1], A[row-1][col+1])
    return min(A[-1])