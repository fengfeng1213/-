def check_brackets(input_string):
    stack = []
    result = [' '] * len(input_string)
    
    for i, char in enumerate(input_string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result[i] = '?'
    
    while stack:
        pos = stack.pop()
        result[pos] = 'x'
    
    return input_string + '\n' + ''.join(result)

# 测试样例
test_cases = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

for test in test_cases:
    print(check_brackets(test))
