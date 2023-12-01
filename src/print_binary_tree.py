from simplify_to_binary_tree import *

standart_file = "final_tree.txt"


def write_to_tree_file(writing, file=standart_file, currentline=None, insertmode=False) -> None:
    if currentline:
        with open(file, "r") as reading_file:
            tree = reading_file.readlines()
        if currentline == len(tree):
            tree[-1] += ("", "\n")[tree[-1][-1] != "\n"]
            tree.append(" ")
        if writing == "repeat":
            tree[currentline] += "".ljust(len(tree[currentline-1]))
        else:
            if all(i == " " for i in writing) and "<---/  \--->" in tree[currentline]:
                tree[currentline+1] = tree[currentline+1][:-1]+writing
            if not insertmode or (insertmode and "<---/  \--->" in tree[currentline]):
                if writing[-1] != "\n":
                    writing += "\n"
                try:
                    if not tree[currentline+1]:
                        tree[currentline+1] = "".ljust(len(tree[currentline]))
                except IndexError:
                    tree.append("".ljust(len(tree[currentline])))
                tree[currentline] = tree[currentline][:-1]+writing
            else:
                if writing[-1] != "\n":
                    writing += "\n"
                writing = "".ljust(len(tree[currentline])) + writing
                tree.insert(currentline, writing)
        with open(file, "w") as writable_file:
            writable_file.writelines(tree)
        return

    with open(file, "a") as writable_file:
        writable_file.write(writing)


def write_binary_element(element, side_space, cont=0, newline=0, currentline=None, insert=False):
    el_space = int(len(element)/2)
    if side_space == "repeat" and all(i == " " for i in element):
        write_to_tree_file("repeat", currentline=currentline)
        return
    side_space = side_space - el_space
    if not cont == -1:
        write_to_tree_file("".ljust(side_space) + element +
                           "".ljust(side_space), currentline=currentline, insertmode=insert)
        if cont and newline:
            newline += -1
            write_to_tree_file(
                "\n", currentline=currentline, insertmode=insert)

    if cont:
        write_to_tree_file("".ljust(side_space-4) + "<---/" + "".ljust(el_space*2) +
                           "\--->" + "".ljust(side_space-4), currentline=currentline, insertmode=insert)
    if newline:
        write_to_tree_file("\n", currentline=currentline, insertmode=insert)


def write_binary_tree(binary_tree: list, linewidth: int, currentline=0) -> None:
    operations = ("^", "*", "/", "+", "-")
    if len(binary_tree) < 2:
        return
    elif len(binary_tree) == 2:
        linewidth = int(linewidth/2)
        saved_current_line = currentline
        saved_linewidth = linewidth
        if isinstance(binary_tree[0], list):
            currentline = saved_current_line
            linewidth = saved_linewidth

            operation1 = "("+binary_tree[0].pop(1)+")"
            write_binary_element(operation1, linewidth,
                                 currentline=currentline, newline=1)
            currentline += 1
            write_binary_element(operation1, linewidth,
                                 cont=-1, currentline=currentline, newline=1)
            currentline += 1
            linewidth = int(linewidth/2)
            for el in binary_tree[0]:
                if not isinstance(el, list):
                    el = "("+el+")"
                    write_binary_element(
                        el, linewidth, currentline=currentline)
                else:
                    if binary_tree[0].index(el) != 0:
                        write_binary_element(
                            " ", linewidth, currentline=currentline+1)
                    write_binary_tree(el, int(linewidth/2), currentline+1)
        else:
            currentline = saved_current_line
            el = "("+binary_tree[0]+")"
            write_binary_element(el, linewidth, currentline=currentline)

        if isinstance(binary_tree[1], list):
            currentline = saved_current_line
            linewidth = saved_linewidth

            operation2 = "("+binary_tree[1].pop(1)+")"
            if not isinstance(binary_tree[0], list):
                write_binary_element(" ", "repeat",
                                     currentline=currentline+1)
            write_binary_element(operation2, linewidth,
                                 currentline=currentline, newline=1)
            currentline += 1
            write_binary_element(operation2, linewidth,
                                 cont=-1, currentline=currentline, newline=1)
            currentline += 1
            linewidth = int(linewidth/2)
            for el in binary_tree[1]:
                if not isinstance(el, list):
                    el = "("+el+")"
                    write_binary_element(
                        el, linewidth, currentline=currentline)
                else:
                    if binary_tree[1].index(el) != 0:
                        write_binary_element(
                            " ", linewidth, currentline=currentline+1)
                    write_binary_tree(el, int(linewidth/2), currentline+1)
        else:
            currentline = saved_current_line
            el = "("+binary_tree[1]+")"
            write_binary_element(el, linewidth, currentline=currentline)

    elif len(binary_tree) == 3:
        for element in binary_tree:
            if not isinstance(element, list) and element in operations:
                if currentline:
                    currentline += -1
                    linewidth = linewidth*2
                    write_binary_element("(" + str(element) + ")",
                                         linewidth, currentline=currentline)
                    write_binary_element("(" + str(element) + ")",
                                         linewidth, cont=-1, currentline=currentline+1, insert=True)
                else:
                    linewidth = int(linewidth / 2)
                    write_binary_element("(" + str(element) + ")",
                                         linewidth, len(binary_tree) > 1, newline=2, currentline=currentline)
                currentline += 2
                binary_tree.pop(binary_tree.index(element))
                write_binary_tree(binary_tree, linewidth,
                                  currentline=currentline)


def main_binary_tree_method(statement: str, isPrint=True) -> list:
    with open(standart_file, "w"):
        pass
    tree = binary_tree_from_arythmetic_statement(statement)
    if isPrint:
        write_binary_tree(tree, 166)
        with open(standart_file, "r") as filey:
            while True:
                buffer = filey.readline()
                if buffer == "":
                    break
                buffer = buffer[:-1].rstrip(" ")
                print(buffer)
    return tree
    # [["6", "+", ["2", "^", ["9", "/", "3"]]], "/", ["11", "-", "4"]]


if __name__ == "__main__":
    main_binary_tree_method("(6 + 2^(9÷3)) ÷ (11 − 4)")

    equation = "15 ÷ (1 + 2))^(10−2×4)"

    

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
