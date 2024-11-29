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


def find_key(data_all):
    end_of_keys = []

    end = -1
    for i in range(len(data_all)):
        if data_all[i] == b"\x02" or data_all[i] == b"\x82":
            if i < end + 6:
                continue
            end_of_keys.append(i)
            end = i

    keys = {}
    for tail, next_tail in zip(end_of_keys, end_of_keys[1:]):
        key = ""
        head = tail + 6
        for letter in data_all[head:next_tail]:
            try:
                key += letter.decode("ascii")
            except:
                break

        if key in keys:
            key = key + "_v2"

        word = get_word(data_all, next_tail)
        value = merge_hexadecimal(word)
        keys[key] = {"head": head, "tail": next_tail, "value": value}

    return keys


def find_index(data_all, msg):
    big_len = len(data_all)
    small_len = len(msg)

    msg = [bytes(m, "utf-8") for m in msg]
    for i in range(big_len - small_len + 1):
        if data_all[i : i + small_len] == msg:
            for j in range(len(data_all[i:])):
                if data_all[i:][j] == b"\x02":
                    print(data_all[i : i + j + 1])
                    return i + j


def get_word(data_all, head, tail):
    word = []
    for i in range(tail, head, -1):
        word.extend(data_all[i])
    return word
