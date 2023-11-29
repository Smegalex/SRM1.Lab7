with open("final_tree.txt", "r") as reading_file:
    tree = reading_file.readlines()
print(tree)
tree[2] = tree[2][:-1]
with open("final_tree.txt", "w") as writable_file:
    writable_file.writelines(tree)
# print(lines)
# binary_tree = [["15", "/", ["1", "+", "2"]], ["10", "-", ["2", "*", "4"]]]
# print("()"+binary_tree[0].pop(1))
