def num_slices(A):
    slices = [0] * len(A)
    count = 0
    for i in range(2, len(A)):
        if A[i] - A[i-1] == A[i-1] - A[i-2]:
            slices[i] = slices[i-1] + 1
            count += slices[i]
    return count
