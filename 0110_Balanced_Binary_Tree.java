/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // returns -1 if root is not balanced, otherwise returns the height of the binary tree
    private int height(TreeNode root) {
        if(root == null) return 0;
        
        int leftHeight = height(root.left);
        int rightHeight = height(root.right);
        
        if(leftHeight == -1 || rightHeight == -1) return -1;
        
        return (Math.abs(leftHeight - rightHeight) <= 1) ? 
                   1 + Math.max(leftHeight, rightHeight) : -1;
    }
    
    public boolean isBalanced(TreeNode root) {
        return height(root) != -1;
    }
}
