import numpy as np
from directed_graph import *
from task_c import *
from print_binary_tree import main_binary_tree_method

matrix1 = np.array([
    [0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1],
])

matrix19 = np.array([
    [0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1],
])

matrix25 = np.array([
    [1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0],
])

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

statement1 = "((2+5)×4-7)÷3"
statement19 = "((8 − 6) × 2 + 3) × 4"
statement25 = "(15 ÷ (1 + 2))^(10−2×4)"


def main7():
    print("Оберіть завдання:")
    print("a. Орієнтованість графа")
    print("b. Представлення арифметичного виразу через бінарне дерево")
    print("c. task_c")
    print("end")


# while True:
main7()
task = input("Введіть варіант: ")

if task.lower() == 'end':
    print("end")
    # break

try:
    if task.lower() in ["a", "b", "c"]:
        print(f"Task {task}.")
        if task == "a":
            directed(matrix1)
            directed(matrix19)
            directed(matrix25)
        elif task == "b":
            print(statement1)
            main_binary_tree_method(statement1, True)
            print("-".ljust(156, "-"))
            print(statement19)
            main_binary_tree_method(statement19, True)
            print("-".ljust(156, "-"))
            print(statement25)
            main_binary_tree_method(statement25, True)

        elif task == "c":
            printExp(expression1)

            printExp(expression2)

            printExp(expression3)
    else:
        print("error")
except ValueError:
    print("error")
