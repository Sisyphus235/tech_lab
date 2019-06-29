# -*- coding: utf8 -*-

"""
LeetCode Question 159.

Given a string S, find the length of the longest substring T that contains at most two distinct characters.

Example:

```
Given S = "eceba",
T is "ece" which its length is 3.
```
"""


def longest_substring_two(s: str) -> int:
    record = {}
    start = 0
    count = 0
    for i in range(len(s)):
        if s[i] in record:
            record[s[i]] += 1
        else:
            if len(record) < 2:
                record[s[i]] = 1
            else:
                cur_count = sum(record.values())
                count = cur_count if cur_count > count else count
                while len(record) > 1:
                    value = record[s[start]] - 1
                    if value == 0:
                        del record[s[start]]
                    else:
                        record[s[start]] = value
                    start += 1
                record[s[i]] = 1

    return count


if __name__ == '__main__':
    print(longest_substring_two('eceba'))
    print(longest_substring_two('ecebbba'))
    print(longest_substring_two('ecebcbba'))
