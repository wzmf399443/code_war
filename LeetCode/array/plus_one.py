import fire


class Solution(object):
    # origin answer
    def plus_one(self, digits: list[int]):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        digits[0] += 1
        for i, v in enumerate(digits):
            if v >= 10:
                digits[i] = 0
                if digits[i] == digits[-1]:
                    digits.append(0)
                digits[i + 1] += 1
        digits.reverse()
        return digits

    # refer others answer
    def plus_one_fix(self, digits: list[int]):
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += c
            if digits[i] >= 10:
                digits[i] = 0
                print(digits)

            else:
                c = 0
                break
        if c == 1:
            digits.insert(0, c)
        return digits


if __name__ == '__main__':
    fire.Fire(Solution)

# import fire


# class Calculator(object):
#     """A simple calculator class."""

#     def double(self, number):
#         return 2 * number


# if __name__ == '__main__':
#     fire.Fire(Calculator)
