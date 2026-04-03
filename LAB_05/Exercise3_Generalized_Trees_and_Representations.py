class GeneralizedCategoryNode:
    def __init__(self, category_id, name="", post_count=0):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.children = []
        self.parent = None


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None  
        self.right = None  



def binary_to_generalized(binary_node):
    if binary_node is None:
        return None

    gen_node = GeneralizedCategoryNode(binary_node.value)

    if binary_node.left:
        
        child = binary_to_generalized(binary_node.left)
        gen_node.children.append(child)
        child.parent = gen_node

        
        sibling = binary_node.left.right
        while sibling:
            sib_node = binary_to_generalized(sibling)
            gen_node.children.append(sib_node)
            sib_node.parent = gen_node
            sibling = sibling.right

    return gen_node


def generalized_to_binary(gen_node):
    if gen_node is None:
        return None

    bin_node = BinaryNode(gen_node.category_id)

    if gen_node.children:
        
        bin_node.left = generalized_to_binary(gen_node.children[0])

        current = bin_node.left

        
        for i in range(1, len(gen_node.children)):
            current.right = generalized_to_binary(gen_node.children[i])
            current = current.right

    return bin_node




def pre_order_generalized(node):
    if node is None:
        return

    print(node.category_id)

    for child in node.children:
        pre_order_generalized(child)



def post_order_generalized(node):
    if node is None:
        return

    for child in node.children:
        post_order_generalized(child)

    print(node.category_id)



from collections import deque

def level_order_generalized(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.category_id)

        for child in node.children:
            queue.append(child)


def calculate_fan_out(node):
    if node is None:
        return 0

    max_children = len(node.children)

    for child in node.children:
        max_children = max(max_children, calculate_fan_out(child))

    return max_children


def calculate_height_generalized(node):
    if node is None:
        return 0

    if not node.children:
        return 1

    return 1 + max(calculate_height_generalized(child) for child in node.children)



def count_nodes_generalized(node):
    if node is None:
        return 0

    count = 1
    for child in node.children:
        count += count_nodes_generalized(child)

    return count



def count_leaves_generalized(node):
    if node is None:
        return 0

    if not node.children:
        return 1

    count = 0
    for child in node.children:
        count += count_leaves_generalized(child)

    return count



def calculate_branching_factor(node):
    total_children = 0
    non_leaf_nodes = 0

    def dfs(current):
        nonlocal total_children, non_leaf_nodes

        if current is None:
            return

        if current.children:
            total_children += len(current.children)
            non_leaf_nodes += 1

        for child in current.children:
            dfs(child)

    dfs(node)

    if non_leaf_nodes == 0:
        return 0

    return total_children / non_leaf_nodes




####################### test ###########################
if __name__ == "__main__":

    ############# case0 ############
    root = GeneralizedCategoryNode(1, "Technology")

    programming = GeneralizedCategoryNode(2, "Programming")
    design = GeneralizedCategoryNode(3, "Design")
    business = GeneralizedCategoryNode(4, "Business")

    python = GeneralizedCategoryNode(5, "Python")
    java = GeneralizedCategoryNode(6, "Java")
    uiux = GeneralizedCategoryNode(7, "UI/UX")
    finance = GeneralizedCategoryNode(8, "Finance")

    
    root.children = [programming, design, business]

    programming.children = [python, java]
    design.children = [uiux]
    business.children = [finance]


    print("Pre-order:")
    pre_order_generalized(root)

    print("Post-order:")
    post_order_generalized(root)

    print("Level-order:")
    level_order_generalized(root)

    
    print("\nMetrics:")
    print("Height:", calculate_height_generalized(root))
    print("Total nodes:", count_nodes_generalized(root))
    print("Leaf nodes:", count_leaves_generalized(root))
    print("Fan-out:", calculate_fan_out(root))
    print("Branching factor:", calculate_branching_factor(root))

   
    print("\nGeneralized → Binary:")
    binary_root = generalized_to_binary(root)

    print("Binary root:", binary_root.value)
    if binary_root.left:
        print("Left (first child):", binary_root.left.value)
    if binary_root.left and binary_root.left.right:
        print("Right sibling of first child:", binary_root.left.right.value)

    
    print("\nBinary → Generalized:")
    new_gen_root = binary_to_generalized(binary_root)

    print("New generalized root:", new_gen_root.category_id)
    print("Children of root:", [child.category_id for child in new_gen_root.children])


###### Case1: Empty Tree########

    print("\n###### case1: Empty Tree########")
    root = None

    print("Height:", calculate_height_generalized(root))
    print("Nodes:", count_nodes_generalized(root))
    print("Leaves:", count_leaves_generalized(root))
    print("Fan-out:", calculate_fan_out(root))
    print("Branching factor:", calculate_branching_factor(root))

    print("Traversal:")
    pre_order_generalized(root)


###### Case2: Only one node ########
    print("\n#### Edge Case: Single Node ########")
    root = GeneralizedCategoryNode(1)

    print("Height:", calculate_height_generalized(root))   # 1
    print("Nodes:", count_nodes_generalized(root))         # 1
    print("Leaves:", count_leaves_generalized(root))       # 1
    print("Fan-out:", calculate_fan_out(root))             # 0
    print("Branching factor:", calculate_branching_factor(root))  # 0

    pre_order_generalized(root)


###### Case3: no children ########

    print("\n########## case3:  no children #######")
    node = GeneralizedCategoryNode(1)

    b = generalized_to_binary(node)
    print("Binary left:", b.left)  






###### case 4 : Unbalanced tree  ########


    print("\n########case 4 : Unbalanced tree##############")
    root = GeneralizedCategoryNode(1)

    a = GeneralizedCategoryNode(2)
    b = GeneralizedCategoryNode(3)
    c = GeneralizedCategoryNode(4)

    d = GeneralizedCategoryNode(5)
    e = GeneralizedCategoryNode(6)

    root.children = [a, b, c]
    a.children = [d]
    d.children = [e]

    print("Height:", calculate_height_generalized(root))
    print("Branching factor:", calculate_branching_factor(root))



######## case5: Chain Tree ######
    print("\n######## case5: Chain Tree ######")
    root = GeneralizedCategoryNode(1)
    current = root

   
    for i in range(2, 5):
        child = GeneralizedCategoryNode(i)
        current.children = [child]
        current = child

    pre_order_generalized(root)
    print("Height:", calculate_height_generalized(root))  
    print("Fan-out:", calculate_fan_out(root))  


