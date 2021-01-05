#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
from leetcode import solution_1_50


class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("单元测试开始：")

    @classmethod
    def tearDownClass(cls):
        print("单元测试结束。")

    def setUp(self):
        self.__test_cls = solution_1_50.Solution()

    def tearDown(self):
        del self.__test_cls

    def test_01(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertListEqual([0, 1], self.__test_cls.twoSum(nums, target))
        print("test 01 ok. ")

    def test_02(self):
        def print_linklist(l):
            while l:
                print(l.val, ",")
                l = l.next

        l1_array = [2, 4, 3]
        l2_array = [5, 6, 4]
        l1_head = solution_1_50.ListNode(l1_array[0])
        l1 = l1_head
        l2_head = solution_1_50.ListNode(l2_array[0])
        l2 = l2_head

        for (x, y) in zip(l1_array[1:], l2_array[1:]):
            temp_1 = solution_1_50.ListNode(x)
            l1.next = temp_1
            l1 = temp_1
            temp_2 = solution_1_50.ListNode(y)
            l2.next = temp_2
            l2 = temp_2

        res_head = self.__test_cls.addTwoNumbers(l1_head, l2_head)

        res = list()
        while res_head:
            res.append(res_head.val)
            res_head = res_head.next

        self.assertListEqual([7, 0, 8], res)

        print("test 02 ok. ")

    def test_03(self):
        self.assertEqual(self.__test_cls.lengthOfLongestSubstring("pwwkew"), 3)
        print("test 03 ok. ")

    def test_04(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(self.__test_cls.findMedianSortedArrays(nums1, nums2), 2.5)
        print("test 04 ok. ")

    def test_05(self):
        self.assertEqual(self.__test_cls.longestPalindrome("babad"), "bab")
        print("test 05 ok. ")

    def test_06(self):
        self.assertEqual(
            self.__test_cls.convert("LEETCODEISHIRING", 3), "LCIRETOESIIGEDHN"
        )
        print("test 06 ok. ")

    def test_07(self):
        self.assertEqual(self.__test_cls.reverse(-123), -321)
        print("test 07 ok. ")

    def test_08(self):
        self.assertEqual(self.__test_cls.myAtoi("42"), 42)
        print("test 08 ok. ")


if __name__ == "__main__":
    # unittest.main()
    __test_cls = SolutionTest()
    __test_cls.setUp()
    __test_cls.test_08()
    __test_cls.tearDown()
