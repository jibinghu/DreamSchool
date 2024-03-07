"""
对于每个输入字符串，检查字符串中的括号是否匹配。
如果左括号没有对应的右括号，在下面标记 'x'。
如果右括号没有对应的左括号，在下面标记 '?'。
"""

def bracketsMatchs(input_strings):
    def bracketsMatch(string):
        # 用栈跟踪左括号的位置
        stack = []
        # 用于标记x或?的位置列表
        markers = [' ' for k in string]

        for i, char in enumerate(string):
            # 以索引位置作为关键点
            if char == '(':
                # 将左括号的索引位置压入栈中
                stack.append(i)
            elif char == ')':
                if stack:
                    # 找到匹配的右括号，从栈中弹出一个左括号的索引位置
                    stack.pop()
                else:
                    # 如果没有匹配的左括号，标记?
                    markers[i] = '?'

        # 对于任何未匹配的左括号，标记x
        for i in stack:
            markers[i] = 'x'
        # print(markers)
        # 返回与输入字符串长度相同的标记字符串
        return ''.join(markers)

    # 对每个输入字符串应用嵌套函数并收集结果
    result = []
    for string in input_strings:
        # 将元素分别添加至result中
        result.append(string)
        result.append(bracketsMatch(string))

    return result

# 给定测试用例
test_strings = []
while True:
    test_string = input()
    if not test_string:
        break
    test_strings.append(test_string)

# 输出
markings = bracketsMatchs(test_strings)
for i in markings:
    print(i,'\n')
