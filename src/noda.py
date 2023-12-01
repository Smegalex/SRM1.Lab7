###
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)
    return []

def postorder_traversal(node):
    if node is not None:
        return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value]
    return []



def evaluate_prefix(expression):
    tokens = expression.split()
    tokens.reverse()
    return evaluate_prefix_helper(tokens.copy())


def evaluate_prefix_helper(tokens):
    if not tokens:
        return None

    token = tokens.pop(0)

    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
        return float(token)

    if token in {'+', '-', '*', '/', '^'}:
        operand1 = evaluate_prefix_helper(tokens.copy())
        operand2 = evaluate_prefix_helper(tokens.copy())

        if token == '+':
            return operand1 + operand2
        elif token == '-':
            return operand1 - operand2
        elif token == '*':
            return operand1 * operand2
        elif token == '/':
            return operand1 / operand2
        elif token == '^':
            return operand1 ** operand2


def evaluate_postfix(expression):
    tokens = expression.split()
    return evaluate_postfix_helper(tokens)


def evaluate_postfix_helper(tokens):
    token = tokens.pop(0)

    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
        return float(token)

    if token in {'+', '-', '*', '/', '^'}:
        operand1 = evaluate_postfix_helper(tokens)
        operand2 = evaluate_postfix_helper(tokens)

        if token == '+':
            return operand1 + operand2
        elif token == '-':
            return operand1 - operand2
        elif token == '*':
            return operand1 * operand2
        elif token == '/':
            return operand1 / operand2
        elif token == '^':
            return operand1 ** operand2




def printExp(root):
    print("Прямий обхід:")
    expression1 = preorder_traversal(root)
    print(expression1)

    # Зворотній обхід:
    print("Зворотний обхід:")
    expression2 = postorder_traversal(root)
    print(expression2)

    result_prefix = evaluate_prefix(' '.join(map(str, expression1)))
    result_postfix = evaluate_postfix(' '.join(map(str, expression2)))

    print(f"Результат прямого обходу: {result_prefix}")
    print(f"Результат зворотнього обходу: {result_postfix}")



if __name__ == "__main__":

    expression1 = Node('/')
    expression1.left = Node('+')
    expression1.right = Node('-')
    expression1.left.left = Node('6')
    expression1.left.right = Node('^')
    expression1.left.right.left = Node('2')
    expression1.left.right.right = Node('/')
    expression1.left.right.right.left = Node('9')
    expression1.left.right.right.right = Node('3')
    expression1.right.left = Node('11')
    expression1.right.right = Node('4')

    expression2 = Node('/')
    expression2.left = Node('+')
    expression2.right = Node('3')
    expression2.left.left = Node('2')
    expression2.left.right = Node('5')
    expression2.left.left.left = Node('×')
    expression2.left.left.right = Node('4')
    expression2.left.left.left.left = Node('+')
    expression2.left.left.left.right = Node('-')
    expression2.left.left.left.left.left = Node('7')

    expression3 = Node('×')
    expression3.left = Node('+')
    expression3.right = Node('4')
    expression3.left.left = Node('×')
    expression3.left.right = Node('3')
    expression3.left.left.left = Node('-')
    expression3.left.left.right = Node('2')
    expression3.left.left.left.left = Node('8')
    expression3.left.left.left.right = Node('6')

    printExp(expression1)
    print()
    printExp(expression2)
    print()
    printExp(expression3)


    # Варіант 24
    # (6 + 2^(9÷3)) ÷ (11 − 4)
    # [["6", "+", ["2", "^", ["9", "/", "3"]]], "/", ["11", "-", "4"]]

    # Варіант 1
    # ((2+5)×4-7)÷3
    # [[[["2", "+", "5"], "*", "4"], "-", "7"], "/", "3"]

    # Варіант 19
    # ((8 − 6) × 2 + 3) × 4
    # [[[["8", "-", "6"], "*", "2"], "+", "3"], "*", "4"]

    # Варіант 25
    # 15 ÷ (1 + 2))^(10−2×4)
    # [["15", "/", ["1", "+", "2"]],"^", ["10", "-", ["2", "*", "4"]]]
