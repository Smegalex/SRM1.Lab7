import numpy as np

def is_symmetrical(mx):
    for i in range(len(mx)):
        for j in range(len(mx)):
            if mx[i][j] != mx[j][i]:
                return False
    return True


def directed(mx):
    print("Граф може бути як неорієнтованим, так і орієнтованим" if is_symmetrical(mx) else "Граф орієнтований")
