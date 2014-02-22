"""
Rotate right to obtain the maximum value which can be obtained by rotating
"""

def ror(num, msb_pos=30):
    lsb = num & 1
    num >>= 1
    if lsb:
        lsb <<= (msb_pos - 1)
    return num | lsb

def max_val_by_ror(num):
    max_val_count = 0
    prev_right_shift = num
    prev = num
    for i in range (1, 31):
        right_shifted = ror(prev)
        if right_shifted > prev_right_shift:
            max_val_count = i
            prev_right_shift = right_shifted
        prev = right_shifted
    return max_val_count


if __name__ == "__main__":
    assert(max_val_by_ror(0) == 0)
    assert(max_val_by_ror(9736) == 11)
