def min_subsequences(source, target):
    # Function to check if all characters of target can be found in source
    def is_subsequence(source, target):
        source_index = 0
        for char in target:
            while source_index < len(source) and source[source_index] != char:
                source_index += 1
            if source_index == len(source):
                return False
            source_index += 1
        return True
    
    # Check if target contains characters not present in source
    if not is_subsequence(source, target):
        return -1
    
    subsequence_count = 0
    target_index = 0

    while target_index < len(target):
        subsequence_count += 1
        source_index = 0

        while target_index < len(target) and source_index < len(source):
            if source[source_index] == target[target_index]:
                target_index += 1
            source_index += 1

    return subsequence_count

# Test cases
print(min_subsequences("abc", "abcbc"))  # Output: 2
print(min_subsequences("abc", "acdbc"))  # Output: -1
print(min_subsequences("xyz", "xzyxz"))  # Output: 3
