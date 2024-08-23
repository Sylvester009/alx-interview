#!/usr/bin/python3

""" UTF-8 Validation
Python script that determines is a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ Determine if a given data set
    represents a valid UTF-8 encoding. 
    """
    # number of bytes in current UTF-8 character
    bytes_num = 0

    # loop through each byte in data set
    for byte in data:
        # if this is start byte of the utf-8 character
        if bytes_num == 0:
            if (byte >> 5) == 0b110:
                bytes_num = 1
            elif (byte >> 4) == 0b1110:
                bytes_num = 2
            elif (byte >> 3) == 0b11110:
                bytes_num = 3
            elif (byte >> 7):
                return False
        else:  # check if it is not a continuation byte
            if (byte >> 6) != 0b10:
                return False
            bytes_num -= 1
    # check for trailing bytes
    return bytes_num == 0
