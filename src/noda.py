
###
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root:
        left_str = inorder_traversal(root.left)
        right_str = inorder_traversal(root.right)
        return f"{left_str} {root.value} {right_str}" if left_str and right_str else f"{left_str}{root.value}{right_str}"
    return ""


def postorder_traversal(root):
    if root:
        left_str = postorder_traversal(root.left)
        right_str = postorder_traversal(root.right)
        return f"{left_str} {right_str} {root.value}".strip() if left_str and right_str else str(root.value)
    return ""


def build_expression_tree(expression):
    stack = []
    current = None

    for char in expression:
        if char.isalnum():
            if current is None:
                current = Node(char)
            else:
                current.value += char
        else:
            if current is not None:
                stack.append(current)
                current = None

            if char == '(':
                continue
            elif char == ')':
                current = stack.pop()
                if stack and stack[-1].value in {'+', '-', '*', '/'}:
                    operator = stack.pop()
                    operator.right = current
                    current = operator
                elif stack and stack[-1].value == '^':
                    operator = stack.pop()
                    operator.right = current
                    current = operator
                stack.append(current)
                current = None
            else:
                stack.append(Node(char))

    if current is not None:
        stack.append(current)

    while len(stack) > 1:
        right = stack.pop()
        operator = stack.pop()
        left = stack.pop()
        operator.left = left
        operator.right = right
        stack.append(operator)

    return stack[0]


if __name__ == "__main__":
    equation = "15 ÷ (1 + 2))^(10−2×4)"

    root = build_expression_tree(equation)

    inorder_result = inorder_traversal(root)
    inorder_result = " ".join(inorder_result.split())
    print("Прямий обхід:")
    print(inorder_result)

    # Зворотній обхід:
    postorder_result = postorder_traversal(root)
    print("\nЗворотній обхід:")
    print(postorder_result)
