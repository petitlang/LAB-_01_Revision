import java.util.List;

public class Ex1Main {
    public static void main(String[] args) {

        // Test Case 1: Empty tree
        System.out.println("Test Case 1: Empty tree");
        CategoryNode emptyRoot = null;

        System.out.println("Tree height: " + CategoryTreeUtils.calculateHeight(emptyRoot));
        System.out.println("Total nodes: " + CategoryTreeUtils.countNodes(emptyRoot));
        System.out.println("Leaf nodes: " + CategoryTreeUtils.countLeaves(emptyRoot));
        System.out.println("Is balanced: " + CategoryTreeUtils.isBalanced(emptyRoot));
        System.out.println("Find category id 1: " + CategoryTreeUtils.findCategory(1, emptyRoot));

        System.out.println();

        // Test Case 2: Single node tree
        System.out.println("Test Case 2: Single node tree");
        CategoryNode singleRoot = new CategoryNode(1, "Technology", 100);

        System.out.println("Tree height: " + CategoryTreeUtils.calculateHeight(singleRoot));
        System.out.println("Total nodes: " + CategoryTreeUtils.countNodes(singleRoot));
        System.out.println("Leaf nodes: " + CategoryTreeUtils.countLeaves(singleRoot));
        System.out.println("Is balanced: " + CategoryTreeUtils.isBalanced(singleRoot));
        System.out.println("Node height of Technology from root: "
                + CategoryTreeUtils.calculateNodeHeight(1, singleRoot));

        System.out.println();

        // Test Case 3: Normal category tree
        System.out.println("Test Case 3: Normal category tree");

        CategoryNode technology = new CategoryNode(1, "Technology", 100);
        CategoryNode programming = new CategoryNode(2, "Programming", 80);
        CategoryNode gadgets = new CategoryNode(3, "Gadgets", 60);
        CategoryNode java = new CategoryNode(4, "Java", 40);
        CategoryNode python = new CategoryNode(5, "Python", 50);
        CategoryNode smartphones = new CategoryNode(6, "Smartphones", 30);
        CategoryNode laptops = new CategoryNode(7, "Laptops", 20);

        CategoryTreeUtils.setLeft(technology, programming);
        CategoryTreeUtils.setRight(technology, gadgets);

        CategoryTreeUtils.setLeft(programming, java);
        CategoryTreeUtils.setRight(programming, python);

        CategoryTreeUtils.setLeft(gadgets, smartphones);
        CategoryTreeUtils.setRight(gadgets, laptops);

        CategoryNode root = technology;

        System.out.println("Tree height: " + CategoryTreeUtils.calculateHeight(root));
        System.out.println("Total nodes: " + CategoryTreeUtils.countNodes(root));
        System.out.println("Leaf nodes: " + CategoryTreeUtils.countLeaves(root));
        System.out.println("Is balanced: " + CategoryTreeUtils.isBalanced(root));

        CategoryNode found = CategoryTreeUtils.findCategory(5, root);
        System.out.println("Find category id 5: " + found);

        List<CategoryNode> path = CategoryTreeUtils.findPathToRoot(5, root);
        System.out.print("Path from Python to root: ");
        CategoryTreeUtils.printPath(path);

        CategoryNode lca = CategoryTreeUtils.lowestCommonAncestor(4, 5, root);
        System.out.println("LCA of Java and Python: " + lca);

        System.out.println("Node height of Python from root: "
                + CategoryTreeUtils.calculateNodeHeight(5, root));

        System.out.println("Is full binary tree: " + CategoryTreeUtils.isFullBinaryTree(root));
        System.out.println("Is perfect binary tree: " + CategoryTreeUtils.isPerfectBinaryTree(root));
        System.out.println("Is complete binary tree: " + CategoryTreeUtils.isCompleteBinaryTree(root));

        System.out.println();

        // Test Case 4: Unbalanced tree
        System.out.println("Test Case 4: Unbalanced tree");

        CategoryNode a = new CategoryNode(10, "Technology", 100);
        CategoryNode b = new CategoryNode(11, "Programming", 80);
        CategoryNode c = new CategoryNode(12, "Java", 40);

        CategoryTreeUtils.setLeft(a, b);
        CategoryTreeUtils.setLeft(b, c);

        CategoryNode unbalancedRoot = a;

        System.out.println("Tree height: " + CategoryTreeUtils.calculateHeight(unbalancedRoot));
        System.out.println("Total nodes: " + CategoryTreeUtils.countNodes(unbalancedRoot));
        System.out.println("Leaf nodes: " + CategoryTreeUtils.countLeaves(unbalancedRoot));
        System.out.println("Is balanced: " + CategoryTreeUtils.isBalanced(unbalancedRoot));
        System.out.println("Is full binary tree: " + CategoryTreeUtils.isFullBinaryTree(unbalancedRoot));
    }
}