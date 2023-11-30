import numpy as np
from directed_graph import *

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


def main7():
    print("Оберіть завдання:")
    print("a. Орієнтованість графа")
    print("b. task_b")
    print("c. task_c")
    print("end")


while True:
    main7()
    task = input("Введіть варіант: ")

    if task.lower() == 'end':
        print("end")
        break

    try:
        if task.lower() in ["a", "b", "c"]:
            print(f"Task {task}.")
            if task == "a":
                directed(matrix1)
                directed(matrix19)
                directed(matrix25)
            #elif task == "b":
            #elif task == "c":
        else:
            print("error")
    except ValueError:
        print("error")
