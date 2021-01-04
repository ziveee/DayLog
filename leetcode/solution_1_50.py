#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def twoSum(self, nums, target):
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i + 1 :]):
                if x + y == target:
                    return [i, i + j + 1]

    def addTwoNumbers(self, l1, l2):
        a = list()
        b = list()
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next

        diff = len(a) - len(b)
        if diff > 0:
            b = b + [0] * diff
        elif diff < 0:
            a = a + [0] * -diff

        res = list()
        flag = False
        for (x, y) in zip(a, b):
            if flag:
                res.append((x + y + 1) % 10)
                if (x + y + 1) > 9:
                    flag = True
                else:
                    flag = False
            else:
                res.append((x + y) % 10)
                if (x + y) > 9:
                    flag = True
                else:
                    flag = False

        if flag:
            res.append(1)

        res = res[::-1]
        last = ListNode(int(res[0]), None)
        for x in res[1:]:
            temp = ListNode(int(x), last)
            last = temp

        return last

    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max_lenth = 0
        temp = ""
        for i, x in enumerate(s):
            if x not in temp:
                temp += x
                if len(temp) > max_lenth:
                    max_lenth = len(temp)
            else:
                temp = temp[temp.find(x) + 1 :]
                temp += x
                if len(temp) > max_lenth:
                    max_lenth = len(temp)

        return max_lenth

    def findMedianSortedArrays(self, nums1, nums2):
        array = nums1 + nums2
        array.sort()

        if len(array) == 1:
            return array[0]

        if len(array) % 2 == 1:
            return array[len(array) // 2]
        else:
            return (array[len(array) // 2 - 1] + array[len(array) // 2]) / 2

    def longestPalindrome(self, s):
        size = len(s)
        if size <= 1:
            return s

        dp = [[False] * size for _ in range(size)]
        max_len = 1
        res = s[0]

        for j in range(size):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            res = s[i : j + 1]
                    else:
                        dp[i][j] = False
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            res = s[i : j + 1]

        return res

    def convert(self, s, numRows):
        if numRows == 1:
            return s

        index_s = 0  # 字符下标
        index_col = 0  # 列下标
        array = ["" for _ in range(numRows)]

        while index_s < len(s):
            if index_col % (numRows - 1) == 0:
                for i in range(numRows):
                    array[i] += s[index_s]
                    index_s += 1
                    if index_s >= len(s):
                        break
                index_col += 1
            else:
                array[numRows - (index_col % (numRows - 1)) - 1] += s[index_s]
                index_s += 1
                index_col += 1

        res = ""
        for x in array:
            res += x

        return res

    def reverse(self, x: int) -> int:
        # int_max = 2147483647
        # int_min = -2147483648
        boundry = 214748364
        res, y = 0, abs(x)
        while y != 0:
            temp = y % 10
            if (res > boundry) or (res == boundry and x > 0 and temp > 7):
                return 0
            if (res > boundry) or (res == boundry and x < 0 and temp > 8):
                return 0
            y //= 10
            res = res * 10 + temp

        return res if x > 0 else -res
