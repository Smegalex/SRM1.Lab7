# with open("final_tree.txt", "r") as reading_file:
#     tree = reading_file.readlines()
# print(tree)
# tree[1] = tree[1][:-1]
# with open("final_tree.txt", "w") as writable_file:
#     writable_file.writelines(tree)
# print(lines)
# binary_tree = [["15", "/", ["1", "+", "2"]], ["10", "-", ["2", "*", "4"]]]
# print("()"+binary_tree[0].pop(1))


statement = ["7", "+", "12", "-", "9", "*", [""]]
my_dict = {1: "+", 2: "-"}
ind = list(my_dict.keys())[
    list(my_dict.values()).index("+")]
statement[ind] = statement[ind-1:ind+2]
statement[ind-1] = ""
statement[ind+1] = ""
statement = list(filter(None, statement))
print(statement)
