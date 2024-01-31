#!/usr/bin/python3
"""UTF8 validation"""


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding"""
    def count_1s(num):
        """Counts the sequence of ones at the begining"""
        count = 0
        for i in range(7, -1, -1):
            if num & (1 << i):  # (1xxxxxxx to xxxxxxx1)
                count += 1
            else:
                break  # stop if 0 is encountered
        return count
    count = 0  # innitialize
    for num in data:
        if not count:  # the begining of new character or termination
            count = count_1s(num)
            if not count:  # termination expected
                continue
            if count == 1 or count > 4:
                # the first number cannot have a single 1
                # a unicode character cannot be more than 4 bytes
                return False
            count -= 1  # decrement to account for firt byte
        else:
            count -= 1  # decrement to account for current byte
            if count_1s(num) != 1:
                # subsequent bytes that are not last can only have 1 at the
                # beginning
                return False
    return count == 0  # the last byte or the only byte
