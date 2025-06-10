/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    private boolean findPath(TreeNode root, List<TreeNode> path, TreeNode target) {
        if (root == null) {                // Java uses lowercase null
            return false;
        }

        path.add(root);                    // include current node

        if (root == target) {              // found it
            return true;
        }

        // search children
        if (findPath(root.left, path, target) ||
            findPath(root.right, path, target)) {
            return true;                   // keep the node in the path
        }

        path.remove(path.size() - 1);      // back-track
        return false;                      // not found in this branch
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
            List<TreeNode> path1 = new ArrayList<>();
        List<TreeNode> path2 = new ArrayList<>();

        // If either node isn’t present in the tree, return null
        if (!findPath(root, path1, p) || !findPath(root, path2, q)) {
            return null;
        }

        /* Walk both paths until the nodes diverge.  
           The last equal node is the LCA. */
        int i = 0;
        while (i < path1.size() && i < path2.size() && path1.get(i) == path2.get(i)) {
            i++;
        }
        return path1.get(i - 1);
    }
}

    