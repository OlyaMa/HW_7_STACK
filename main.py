from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def is_balanced(str_):
    s = Stack()
    balance = True
    index = 0
    while index < len(str_) and balance:
        symbol = str_[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balance = False
        index += 1
    if balance and s.is_empty():
        return 'Сбалансировано'
    else:
        return 'Несбалансировано'


def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


if __name__ == '__main__':
    string_1 = '(((([{}]))))'
    string_2 = '[([])((([[[]]])))]{()}'
    string_3 = '{{[()]}}'
    string_4 = '}{}'
    string_5 = '{{[(])]}}'
    string_6 = '[[{())}]'
    print(is_balanced(string_1))
    print(is_balanced(string_2))
    print(is_balanced(string_3))
    print(is_balanced(string_4))
    print(is_balanced(string_5))
    print(is_balanced(string_6))
