import numpy as np
from directed_graph import *
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

        # elif task == "c":
    else:
        print("error")
except ValueError:
    print("error")
