standart_file = "final_tree.txt"


def standartise_statement(statement):
    return statement.replace(" ", "").replace("÷", "/").replace(":", "/").replace("×", "*").replace("·", "*").replace("−", "-")


def binary_tree_from_arythmetic_statement(statement):
    tree = []

    statement = standartise_statement(statement)
    if "^" in statement:
        statement = list(statement.split("^", 1))
        statement.insert(1, "^")
        if statement[0][-1] == ")":
            statement[0] = statement[-1][1:-1]


def write_to_tree_file(writing, file=standart_file, currentline=None, insertmode=False) -> None:
    if currentline:
        with open(file, "r") as reading_file:
            tree = reading_file.readlines()
        if currentline == len(tree):
            tree[-1] += "\n"
            tree.append(" ")
        if not insertmode:
            tree[currentline] = tree[currentline][:-1]+writing
        else:
            if writable_file[-1] != "\n":
                writable_file += "\n"
            tree.insert(currentline, writable_file)
        with open(file, "w") as writable_file:
            writable_file.writelines(tree)
        return

    with open(file, "a") as writable_file:
        writable_file.write(writing)


def write_binary_element(element, left_space, cont=0, newline=0, currentline=None):
    el_space = int(len(element)/2)
    left_space = left_space - el_space
    if not cont == -1:
        write_to_tree_file("".ljust(left_space) + element +
                           "".ljust(left_space), currentline=currentline)
        if cont and newline:
            newline += -1
            write_to_tree_file("\n", currentline=currentline)

    if cont:
        write_to_tree_file("".ljust(left_space-4) + "<---/" + "".ljust(el_space*2) +
                           "\--->" + "".ljust(left_space-4), currentline=currentline)
    if newline:
        write_to_tree_file("\n", currentline=currentline)


def write_binary_tree(binary_tree: list, linewidth: int, currentline=0) -> None:
    operations = ("^", "*", "/", "+", "-")
    if len(binary_tree) < 2:
        return
    elif len(binary_tree) == 2:
        linewidth = int(linewidth/2)

        if isinstance(binary_tree[0], list):
            operation1 = "("+binary_tree[0].pop(1)+")"
            operation2 = "("+binary_tree[1].pop(1)+")"

            write_binary_element(operation1, linewidth)
            write_binary_element(operation2, linewidth, newline=1)
            currentline += 1
            write_binary_element(operation1, linewidth, -1)
            write_binary_element(operation2, linewidth, -1, newline=1)
            currentline += 1

            linewidth = int(linewidth/2)
        for el in binary_tree[0]:
            if not isinstance(el, list):
                el = "("+el+")"
                write_binary_element(el, linewidth)
            else:
                if binary_tree[0].index(el) != 0:
                    write_binary_element(
                        " ", linewidth, currentline=currentline+1)
                write_binary_tree(el, int(linewidth/2), currentline+1)

    elif len(binary_tree) == 3:
        for element in binary_tree:
            if not isinstance(element, list) and element in operations:
                insert = False
                if currentline:
                    insert = True
                    currentline += -1
                    linewidth = linewidth*2
                else:
                    linewidth = int(linewidth / 2)
                write_binary_element("(" + str(element) + ")",
                                     linewidth, len(binary_tree) > 1, newline=2, currentline=currentline)
                currentline += 2
                binary_tree.pop(binary_tree.index(element))
                write_binary_tree(binary_tree, linewidth,
                                  currentline=currentline)


if __name__ == "__main__":
    # standart_file =
    with open(standart_file, "w"):
        pass
    binary_tree_from_arythmetic_statement("15 ÷ (1 + 2))^(10−2×4)")
    write_binary_tree([["15", "/", ["1", "+", "2"]],
                       "^", ["10", "-", ["2", "*", "4"]]], 166)
