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

    def myAtoi(self, s):
        def check_num(x):  # 判断字符x是否为数字
            if x not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return False
            return True

        s = s.strip(" ")  # 删除字符串开头空格
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return int(s[0]) if check_num(s[0]) else 0

        if s[0] not in ["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return 0

        if s[:2] in ["+-", "-+", "++", "--"]:
            return 0

        int_max = 2147483647
        int_min = -2147483648
        boundry = 214748364

        if s[0] in ["+", "-"]:  # 符号开头
            res = "" if s[0] == "+" else "-"
            insert_flag = False  # 代表不插入(即为0)
            for i, x in enumerate(s[1:]):
                if check_num(x):  # 当前位是数字
                    if not insert_flag and x != "0":  # 判断是否插入(排除符号后边的0)
                        insert_flag = True

                    if insert_flag:
                        res += x
                        if s[0] == "-":
                            if len(res[1:]) == 9 and int(res[1:]) > boundry:
                                return int_min
                            if (
                                len(res[1:]) == 10
                                and int(res[1:10]) == boundry
                                and int(x) > 8
                            ):
                                return int_min
                            if len(res[1:]) > 10:
                                return int_min
                        else:
                            if len(res) == 9 and int(res) > boundry:
                                return int_max
                            if (
                                len(res) == 10
                                and int(res[:9]) == boundry
                                and int(x) > 7
                            ):
                                return int_max
                            if len(res) > 10:
                                return int_max
                else:
                    return int(res) if len(res) > 0 and insert_flag else 0
            return int(res) if insert_flag else 0
        else:  # 数字开头
            res = ""
            insert_flag = False  # 代表不插入(即为0)
            for i, x in enumerate(s):
                if check_num(x):  # 当前位是数字
                    if not insert_flag and x != "0":  # 判断是否插入(排除最前面的0)
                        insert_flag = True

                    if insert_flag:
                        res += x
                        if len(res) == 9 and int(res) > boundry:
                            return int_max
                        if len(res) == 10 and int(res[:9]) == boundry and int(x) > 7:
                            return int_max
                        if len(res) > 10:
                            return int_max
                else:
                    return int(res) if len(res) > 0 else 0

            return int(res) if insert_flag else 0

    def myAtoi_re(self, s):
        import re

        # int_max = 2147483647
        # int_min = -2147483648
        # s = s.lstrip()
        # num_re = re.compile(r"^[\+\-]?\d+")
        # num = num_re.findall(s)
        # num = int(*num)
        # return max(min(num, int_max), int_min)
        return max(
            min(int(*re.findall(r"^[\+\-]?\d+", s.lstrip(" "))), 2 ** 31 - 1),
            -(2 ** 31),
        )

    def myAtoi_automaton(self, s):
        s = s.lstrip(" ")
        table = {
            # +/-, number, other
            "start": ["signed", "number", "end"],
            "signed": ["end", "number", "end"],
            "number": ["end", "number", "end"],
            "other": ["end", "end", "end"],
        }

        def is_number(c):
            if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return True
            return False

        def get_col(c):
            if c in ["+", "-"]:
                return 0
            elif is_number(c):
                return 1
            return 2

        ans = 0
        sign = 1
        state = "start"
        int_max = 2147483647
        int_min = -2147483648

        def get_c(c):
            nonlocal state, ans, sign
            state = table[state][get_col(c)]
            if state == "number":
                if ans > 214748364:
                    return int_max if sign == 1 else int_min

                elif ans == 214748364:
                    return int_max if sign == 1 and int(c) > 7 else ans * 10 + int(c)
                    return (
                        int_min
                        if sign == -1 and int(c) > 8
                        else sign * (ans * 10 + int(c))
                    )
                ans = ans * 10 + int(c)

            elif state == "signed":
                sign = 1 if c == "+" else -1

        for x in s:
            if get_c(x):
                return get_c(x)
            if state == "end":
                return sign * ans

        return sign * ans

    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        return False

    def isPalindrome_1(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        seq = list()
        while x // 10 != 0:
            seq.append(x % 10)
            x = x // 10
        seq.append(x % 10)

        for i in range(len(seq) // 2):
            if seq[i] != seq[-i - 1]:
                return False

        return True


test = Solution()
print(test.isPalindrome_1(1001))
