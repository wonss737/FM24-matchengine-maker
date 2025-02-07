def merge_hexadecimal(word):
    convert = "0x"
    for data in word:
        convert += f"{data:02x}"
    return int(convert, 16)


def split_hexadecimal(num, split_num=2):
    """
    split_num : split hexadecimal by split_num
        ex ) x0004baf0 -> b'\x00', b'\x04', b'\xba', b'\xf0'
    """
    replaced = f"{num:08x}"
    split_replaced = []
    for i in range(0, len(replaced), split_num):
        temp = replaced[i : i + split_num]
        binary = bytes.fromhex(temp)
        split_replaced.append(binary)
    return split_replaced


def get_word(data_all, head, tail):
    word = []
    for i in range(tail, head, -1):
        word.extend(data_all[i])
    return word
