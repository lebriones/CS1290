def longest_chain(pairs):
    chains = [1] * len(pairs)
    for i in range(len(pairs)):
        for j in range(i):
            if pairs[j][1] < pairs[i][0]:
                chains[i] = max(chains[i], chains[j] + 1)
    return max(chains)
