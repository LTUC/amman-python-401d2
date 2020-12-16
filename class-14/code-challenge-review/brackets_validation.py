import pysnooper

# @pysnooper.snoop()
def multi_bracket_validation(str):
    processor = []
    open_brackets = {'(':')', '[':']', '{':'}'}
    for char in str:
        if char in open_brackets.keys():
            processor.append(char)
        elif char in open_brackets.values():
            if len(processor) == 0:
                return False
            temp = processor.pop()
            if char!= open_brackets[temp]:
                return False
        else:
            continue
    if len(processor) != 0:
        return False
    return True


if __name__=='__main__':
    print(multi_bracket_validation('()[[Extra Characters]]'))
    print(multi_bracket_validation('{}{Code}[Fellows](())'))
    print(multi_bracket_validation('[({}]'))
    print(multi_bracket_validation('{'))
    print(multi_bracket_validation(']'))
    print(multi_bracket_validation('{(})'))


