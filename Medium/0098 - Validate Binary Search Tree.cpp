class Solution {
public:
    bool boundary(TreeNode* node, long double left_bound, long double right_bound)
    {
        if(node == NULL)
            return true;
            
        if (not(node->val < right_bound && node->val > left_bound))
            return false;
            
        return boundary(node->left, left_bound, node->val) && boundary(node->right, node->val, right_bound);
    }
    
    bool isValidBST(TreeNode* root) 
    {   
        return boundary(root, -INFINITY, INFINITY);   
    }
};
