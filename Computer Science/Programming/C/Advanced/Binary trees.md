# Binary trees
[[C]]
---

### Introduction

A Binary Tree is a type of data structure in which each node has at most two children (left child and right child). Binary trees are used to implement binary search trees and binary heaps, and are used for efficient searching and sorting. A binary tree is a special case of a K-ary tree, where k is 2. Common operations for binary trees include insertion, deletion, and traversal. The difficulty of performing these operations varies if the tree is balanced and also whether the nodes are leaf nodes or branch nodes. For **balanced trees** the depth of the left and right subtrees of every node differ by 1 or less. This allows for a predictable **depth** also known as **height**. This is the measure of a node from root to leaf, where root is 0 and sebsequent nodes are (1,2..n). This can be expressed by the integer part of log2(n) where n is the number of nodes in the tree.

```c
        g                  s                  9
       / \                / \                / \
      b   m              f   u              5   13
     / \                    / \                /  \
    c   d                  t   y              11  15
```

The operations performed on trees requires searching in one of two main ways: Depth First Search and Breadth-first search. **Depth-first search (DFS)** is an algorithm for traversing or searching tree or graph data structures. One starts at the root and explores as far as possible along each branch before backtracking. There are three types of depth first search traversal: **pre-order** visit, left, right, **in-order** left, visit, right, **post-order** left, right, visit. **Breadth-first search (BFS)** is an algorithm for traversing or searching tree or graph structures. In level-order, where we visit every node on a level before going to a lower level.