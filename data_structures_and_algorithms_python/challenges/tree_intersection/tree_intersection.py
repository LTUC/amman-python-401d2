from data_structures_and_algorithms_python.data_structure.tree.tree import *



def tree_intersection(tree1, tree2):
    if tree1.root and tree2.root:
        list1 = set(tree1.preOrder())
        list2 = tree2.preOrder()
        output = []
        for i in list2:
            if i in list1:
                output.append(i)
        return set(output)
    else:
        return ('the tree is empty')



