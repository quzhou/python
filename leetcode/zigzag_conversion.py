"""https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
    string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        holder = []
        for i in range(numRows):
            holder.append([])

        line = 0
        down = True
        for i in range(len(s)):
            sub = holder[line]
            sub.append(s[i])

            if line == (numRows - 1):
                down = False
                line -= 1
            elif line == 0:
                down = True
                line += 1
            elif down:
                line += 1
            else:
                line -= 1

        ret = ""
        for i in range(numRows):
            ret += "".join(holder[i])

        return ret


    def convert2(self, s, numRows):
        if numRows < 2:
            return s
        step, ret = numRows * 2 - 2, ""
        for i in range(numRows):
            for j in range(i, len(s), step):
                ret += s[j]
                if 0 < i < numRows - 1:
                    gap = (numRows - i) * 2 - 2
                    if j + gap < len(s):
                        ret += s[j + gap]

        return ret

if __name__ == "__main__":
    print Solution().convert2("ABC", 2)
