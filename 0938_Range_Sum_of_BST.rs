// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        fn rec(root: &Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
            match root {
                None => 0,
                Some(x) => {
                    let x = (*x).borrow();
                    (if low <= x.val && x.val <= high { x.val } else { 0 }) +
                    rec(&x.left, low, high) +
                    rec(&x.right, low, high)
                },
            }
        }
        
        rec(&root, low, high)
    }
}
