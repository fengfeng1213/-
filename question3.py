import itertools

def mean(seq):
    return sum(seq) / len(seq)

def median(seq):
    sorted_seq = sorted(seq)
    n = len(sorted_seq)
    if n % 2 == 1:
        return sorted_seq[n // 2]
    else:
        return (sorted_seq[n // 2 - 1] + sorted_seq[n // 2]) / 2

def max_val_subsequence(n, a):
    max_val = float('-inf')
    
    for i in range(1, 2 ** n):
        subseq = [a[j] for j in range(n) if (i & (1 << j))]
        if subseq:
            val = mean(subseq) - median(subseq)
            max_val = max(max_val, val)
    
    return max_val

# Sample input
n = 4
a = [1, 3, 5, 9]

# Output the result
result = max_val_subsequence(n, a)
print(result)

