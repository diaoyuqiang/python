def get_bit(bit, index):
    """
    取单个bit对应位值
    """
    if bit & (1 << index):
        return 1
    else:
        return 0

a = get_bit(1, 1)
print("a:", a)