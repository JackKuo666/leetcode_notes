# leetcode_notes
这个是我在刷leetcode[Top Interview Questions 150](https://leetcode.com/problemset/top-interview-questions/)的时候的一些笔记

灵感来自：

顺序刷：https://github.com/qiyuangong/leetcode

分类刷：https://github.com/kamyu104/LeetCode-Solutions

Pythonic：https://github.com/cy69855522/Short-LeetCode-Python-Solutions


这里主要按照两个方向刷题：

1.顺序刷

Top Interview Questions 150 : https://leetcode.com/problemset/top-interview-questions/

2.分类刷

Top Interview Questions：easy | medium | hard ：https://leetcode.com/explore/interview/card/top-interview-questions-easy/


3.其他

Python内置函数的时间复杂度：https://wiki.python.org/moin/TimeComplexity


| # | Title | Solution | Basic idea (One line) | note |
|---| ----- | -------- | --------------------- | ---- |
| 1 | [两数之和](https://leetcode.com/problems/two-sum/) | [Python](https://github.com/JackKuo666/leetcode_notes/blob/master/1.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.py)| 1. Hash O(n) and O(n) space.<br>2. 暴力遍历法 O(n^2) and O(1).<br>3.sort+双指针 >O(n) and O(n) | 没排序的输入，最好使用Hashmap法|
| 2 | [两个链表数字之和](https://leetcode.com/problems/add-two-numbers/) | [Python](https://github.com/JackKuo666/leetcode_notes/blob/master/2.%E4%B8%A4%E4%B8%AA%E9%93%BE%E8%A1%A8%E6%95%B0%E5%AD%97%E4%B9%8B%E5%92%8C.py) | 1.分布遍历两个链表，转成数字，相加，然后转成链表 O(n) and O(n) | |
| 3 | [最长无重复子字符串](https://leetcode.com/problems/longest-substring-without-repeating-characters/)| [Python](https://github.com/JackKuo666/leetcode_notes/blob/master/3.%E6%9C%80%E9%95%BF%E6%97%A0%E9%87%8D%E5%A4%8D%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.py) | 1.哈希表+单指针 O(n) and O(1) |  |
| 4 | [两个排序列表的中位数](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Python](https://github.com/JackKuo666/leetcode_notes/blob/master/4.%E4%B8%A4%E4%B8%AA%E6%8E%92%E5%BA%8F%E5%88%97%E8%A1%A8%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.py) | 1.常规解法：合并两个列表+sort() O((m+n)log(m+n))<br>2.二分查找法 O(log(m+n)) | 二分查找法解析见[这里](https://www.cnblogs.com/zuoyuan/p/3759682.html) | 
| 5 | [最长回文子串](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/JackKuo666/leetcode_notes/blob/master/5.%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.py) |1.[DP](https://blog.csdn.net/qq_20141867/article/details/81253533): O(n^2) and O(n^2)<br>2.[manacher算法](https://blog.csdn.net/tuobadon/article/details/78989601) O(n) and O(n) | 解析请看[这里](https://blog.csdn.net/weixin_37251044/article/details/89856019) |
| 6 | [Z字形变换解析](https://leetcode.com/problems/zigzag-conversion/) | [Python](https://github.com/JackKuo666/leetcode_notes/blob/master/6.Z%E5%AD%97%E5%BD%A2%E5%8F%98%E6%8D%A2.py) | 1.创建一个list保存，然后打印出来 O(n) and O(n) | 解析见我的[博客](https://blog.csdn.net/weixin_37251044/article/details/85398417) |






python笔记:
```py
1.dic.get("a", -1) # 返回dic中“a”的value，如果没有，返回“-1”
```





数组：

    1 Two Sum（系列）
    57 有序数组中和为s的两个数（
    167 Two Sum II - Input array is sorted）
    3Sum（系列） + 4sum
    Contains Duplicate
    3 数组中重复的数字（287. Find the Duplicate Number）
    26 Remove Duplicates from Sorted Array
    39 数组中出现次数超过一半的数字
    53 数字在排序数组中出现的次数
    旋转数组（189. Rotate Array）
    Intersection of Two Arrays（系列）
    228. Summary Ranges
    66 构建乘积数组（cnblogs）
    21 调整数组顺序使奇数位于偶数前面
    61 扑克牌中的顺子
    45 把数组排成最小的数
    51 数组中的逆序对
    Increasing Triplet Subsequence
    Plus One
    Move Zeroes
    Valid Sudoku
    Rotate Image

矩阵

    4 有序矩阵中的查找（ 74. Search a 2D Matrix ）（系列）
    29 顺时针打印矩阵（54. Spiral Matrix）（系列）
    Kth Smallest Element in a Sorted Matrix
    Set Matrix Zeroes(cnblogs)

位运算

    位运算规律总结
    15 二进制中1的个数（191. Number of 1 Bits）
    56 数组中只出现一次的数字（136. Single Number）（系列）

特殊数与数位

    204. Count Primes
    263. Ugly Number（系列）
    43 1~n整数中1出现的次数 (233. Number of Digit One )
    44 数字序列中某一位的数字(400. Nth Digit)

字符串

    50 第一个只出现一次的字符（387. First Unique Character in a String）
    5 替换空格
    Reverse String
    Reverse Integer
    58 翻转字符串（翻转单词与左旋转字符串）
    67 把字符串转成整数
    String to Integer (atoi)
    Implement strStr()（cnblogs）
    38 字符串的排列（全排列问题）
    Longest Common Prefix(cnblogs)
    Valid Parentheses（括号对）(cnblogs)
    Valid Palindrome(回文词系列)
    Longest Palindromic Substring
    242. Valid Anagram (变位词系列)
    48 最长不含重复字符的子字符串（3. Longest Substring Without Repeating Characters）
    Count and Say
    19 正则表达式匹配（hard，了解即可）
    20 表示数值的字符串（了解即可）

栈和队列

    9.1 用队列实现栈（225. Implement Stack using Queues）
    9.2 用栈实现队列（232. Implement Queue using Stacks）
    30 包含min函数的栈（155. Min Stack）
    31 栈的压入、弹出序列
    59 队列（滑动窗口）的最大值

链表

    14 反转链表 206. Reverse Linked List（系列）
    6 从尾到头打印链表
    18 删除链表中的结点（237. Delete Node in a Linked List）
    22 删除链表中倒数第k个结点（19. Remove Nth Node From End of List）(cnblogs)
    52 两个链表的第一个公共结点（Intersection of Two Linked Lists）
    23 有环链表问题-链表中环的入口结点（141. Linked List Cycle）
    25 合并两个排序的链表（系列）（21. Merge Two Sorted Lists）
    35 复杂链表的复制（138. Copy List with Random Pointer）
    Add Two Numbers
    328. Odd Even Linked List
    Palindrome Linked List

树

    二叉树的遍历总结（前序、中序、后序、层序、 之字形层序、垂直序）
    二叉查找树的查找、插入、删除
    68 树中两个节点的最低公共祖先
    104. Maximum Depth of Binary Tree
    110. Balanced Binary Tree
    28 对称二叉树（101. Symmetric Tree）
    27 二叉树的镜像
    26 树的子结构（572. Subtree of Another Tree）
    34 二叉树中和为某一值的路径（112. Path Sum）
    124. Binary Tree Maximum Path Sum
    37 序列化二叉树（297. Serialize and Deserialize Binary Tree）(cnblogs)
    7 重建二叉树（系列）
    Validate Binary Search Tree
    36 二叉搜索树与双向链表
    33 判断某序列是否为二叉搜索树的后序序列
    Kth Smallest Element in a BST(cnblogs)
    Convert Sorted Array to Binary Search Tree(cnblogs)
    Populating Next Right Pointers in Each Node
    8 二叉树中序遍历的下一个结点

查找与排序

    二分查找小结
    40 最小的k个数（对应Kth Largest Element in an Array）
    41 数据流中的中位数（295. Find Median from Data Stream）
    Median of Two Sorted Arrays
    Merge Sorted Array
    33 Search in Rotated Sorted Array(系列)(cnblogs)
    11旋转数组的最小数字（153. Find Minimum in Rotated Sorted Array）（系列）
    Search for a Range
    Find Peak Element
    First Bad Version
    Sort Colors(cnblogs)
    Top K Frequent Elements
    Merge Intervals(cnblogs)
    Wiggle Sort（系列）

动态规划与贪婪法

    70 Climbing Stairs
    14 剪绳子
    剑指Offer-46：把数字翻译成字符串
    42 连续子数组的最大和（53. Maximum Subarray）
    Maximum Product Subarray
    《算法导论》动态规划、贪婪法与分治法ppt
    47：礼物的最大价值
    House Robber（系列）
    Unique Paths（系列）
    Longest Increasing Subsequence
    121. Best Time to Buy and Sell Stock（系列）
    Jump Game（系列）
    Coin Change（系列）
    Burst Balloons
    Word Break（系列）
    背包问题总结

回溯法和暴力枚举法

    排列与组合
    12 矩阵中的字符串查找（79. Word Search 系列）
    13 机器人的运动范围
    Generate Parentheses
    Letter Combinations of a Phone Number
    Number of Islands
    Subsets（系列）

分治法

    16 数值的整数次方（50. Pow(x, n)）
    42 连续子数组的最大和（53. Maximum Subarray）
    Sqrt(x)

发散思维题

    17 打印从1到最大的n位数
    43 n个骰子的点数
    62 圆圈中最后剩下的数字（约瑟夫环问题）
    64 求1+2+…+n
    65 不用加减乘除做加法
    231. Power of Two（系列）
    Fizz Buzz(cnblogs)
    Roman to Integer
    Shuffle an Array

