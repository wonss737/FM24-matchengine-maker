import os
import sys
import json


def load_loacation():
    return {
    "acceleration_scaler": {
        "head": 41,
        "tail": 45,
        "head2": 2864,
        "tail2": 2868,
    },
    "base_top_speed": {
        "head": 61,
        "tail": 65,
        "head2": 2884,
        "tail2": 2888,
    },
    "basic_header_speed": {
        "head": 85,
        "tail": 89,
        "head2": 2908,
        "tail2": 2912,
    },
    "fast_jog_speed": {
        "head": 105,
        "tail": 109,
        "head2": 2928,
        "tail2": 2932,
    },
    "fast_walk_speed": {
        "head": 126,
        "tail": 130,
        "head2": 2949,
        "tail2": 2953,
    },
    "hard_kick_speed": {
        "head": 147,
        "tail": 151,
        "head2": 2970,
        "tail2": 2974,
    },
    "jog_speed": {
        "head": 162,
        "tail": 166,
        "head2": 2985,
        "tail2": 2989,
    },
    "medium_kick_speed": {
        "head": 185,
        "tail": 189,
        "head2": 3008,
        "tail2": 3012,
    },
    "medium_to_moderate_kick_speed": {
        "head": 220,
        "tail": 224,
        "head2": 3043,
        "tail2": 3047,
    },
    "min_delay_for_ball_lunge_do": {
        "head": 253,
        "tail": 257,
        "head2": 3076,
        "tail2": 3080,
    },
    "min_delay_for_ball_lunge_receive": {
        "head": 291,
        "tail": 295,
        "head2": 3114,
        "tail2": 3118,
    },
    "min_delay_for_block_tackle_do": {
        "head": 326,
        "tail": 330,
        "head2": 3149,
        "tail2": 3153,
    },
    "min_delay_for_block_tackle_receive": {
        "head": 366,
        "tail": 370,
        "head2": 3189,
        "tail2": 3193,
    },
    "min_delay_for_celebrating_a_goal": {
        "head": 404,
        "tail": 408,
        "head2": 3227,
        "tail2": 3231,
    },
    "min_delay_for_deflect_ball_do": {
        "head": 439,
        "tail": 443,
        "head2": 3262,
        "tail2": 3266,
    },
    "min_delay_for_deflect_ball_receive": {
        "head": 479,
        "tail": 483,
        "head2": 3302,
        "tail2": 3306,
    },
    "min_delay_for_diving_header": {
        "head": 512,
        "tail": 516,
        "head2": 3335,
        "tail2": 3339,
    },
    "min_delay_for_foot_up_in_tackle_do": {
        "head": 552,
        "tail": 556,
        "head2": 3375,
        "tail2": 3379,
    },
    "min_delay_for_foot_up_in_tackle_receive": {
        "head": 597,
        "tail": 601,
        "head2": 3420,
        "tail2": 3424,
    },
    "min_delay_for_force_opponent_to_lose_ball_do": {
        "head": 647,
        "tail": 651,
        "head2": 3470,
        "tail2": 3474,
    },
    "min_delay_for_force_opponent_to_lose_ball_receive": {
        "head": 702,
        "tail": 706,
        "head2": 3525,
        "tail2": 3529,
    },
    "min_delay_for_getting_injured": {
        "head": 737,
        "tail": 741,
        "head2": 3560,
        "tail2": 3564,
    },
    "min_delay_for_normal_header": {
        "head": 770,
        "tail": 774,
        "head2": 3593,
        "tail2": 3597,
    },
    "min_delay_for_obstruct_do": {
        "head": 801,
        "tail": 805,
        "head2": 3624,
        "tail2": 3628,
    },
    "min_delay_for_obstruct_receive": {
        "head": 837,
        "tail": 841,
        "head2": 3660,
        "tail2": 3664,
    },
    "min_delay_for_player_stop_to_avoid_collision": {
        "head": 887,
        "tail": 891,
        "head2": 3710,
        "tail2": 3714,
    },
    "min_delay_for_push_opponen_receive": {
        "head": 927,
        "tail": 931,
        "head2": 3750,
        "tail2": 3754,
    },
    "min_delay_for_push_opponent_do": {
        "head": 963,
        "tail": 967,
        "head2": 3786,
        "tail2": 3790,
    },
    "min_delay_for_shirt_tug_do": {
        "head": 994,
        "tail": 995,
        "head2": 3817,
        "tail2": 3818,
    },
    "min_delay_for_shirt_tug_receive": {
        "head": 1028,
        "tail": 1032,
        "head2": 3851,
        "tail2": 3855,
    },
    "min_delay_for_shoulder_charge_do": {
        "head": 1066,
        "tail": 1070,
        "head2": 3889,
        "tail2": 3893,
    },
    "min_delay_for_shoulder_charge_receive": {
        "head": 1109,
        "tail": 1113,
        "head2": 3932,
        "tail2": 3936,
    },
    "min_delay_for_slide_tackle_do": {
        "head": 1144,
        "tail": 1148,
        "head2": 3967,
        "tail2": 3971,
    },
    "min_delay_for_slide_tackle_receive": {
        "head": 1184,
        "tail": 1188,
        "head2": 4007,
        "tail2": 4011,
    },
    "min_delay_for_trip_do": {
        "head": 1211,
        "tail": 1215,
        "head2": 4034,
        "tail2": 4038,
    },
    "min_delay_for_trip_receive": {
        "head": 1243,
        "tail": 1247,
        "head2": 4066,
        "tail2": 4070,
    },
    "min_delay_for_two_footed_tackle_do": {
        "head": 1283,
        "tail": 1287,
        "head2": 4106,
        "tail2": 4110,
    },
    "min_delay_for_two_footed_tackle_receive": {
        "head": 1328,
        "tail": 1332,
        "head2": 4151,
        "tail2": 4155,
    },
    "min_delay_for_violent_act_do": {
        "head": 1362,
        "tail": 1366,
        "head2": 4185,
        "tail2": 4189,
    },
    "min_delay_for_violent_act_receive": {
        "head": 1401,
        "tail": 1405,
        "head2": 4224,
        "tail2": 4228,
    },
    "min_delay_keeper_drop_ball_for_distribution": {
        "head": 1450,
        "tail": 1454,
        "head2": 4273,
        "tail2": 4277,
    },
    "min_delay_keeper_save_dive_and_hold_ball": {
        "head": 1496,
        "tail": 1500,
        "head2": 4319,
        "tail2": 4323,
    },
    "min_delay_keeper_save_dive_but_not_held": {
        "head": 1541,
        "tail": 1545,
        "head2": 4364,
        "tail2": 4368,
    },
    "min_delay_keeper_save_intentionally_drop_ball": {
        "head": 1592,
        "tail": 1596,
        "head2": 4415,
        "tail2": 4419,
    },
    "min_delay_keeper_save_no_dive_hold_ball": {
        "head": 1637,
        "tail": 1641,
        "head2": 4460,
        "tail2": 4464,
    },
    "min_delay_keeper_save_no_dive_not_held": {
        "head": 1681,
        "tail": 1685,
        "head2": 4504,
        "tail2": 4508,
    },
    "min_delay_keeper_save_with_outreached_foot": {
        "head": 1729,
        "tail": 1733,
        "head2": 4552,
        "tail2": 4556,
    },
    "min_extra_delay_for_falling_down_before_injury": {
        "head": 1781,
        "tail": 1785,
        "head2": 4604,
        "tail2": 4608,
    },
    "moderate_jog_speed": {
        "head": 1886,
        "tail": 1890,
        "head2": 4705,
        "tail2": 4709,
    },
    "moderate_kick_speed": {
        "head": 1911,
        "tail": 1915,
        "head2": 4730,
        "tail2": 4734,
    },
    "quite_hard_kick_speed": {
        "head": 1938,
        "tail": 1942,
        "head2": 4757,
        "tail2": 4761,
    },
    "run_speed": {
        "head": 1953,
        "tail": 1957,
        "head2": 4772,
        "tail2": 4776,
    },
    "slow_jog_speed": {
        "head": 1973,
        "tail": 1977,
        "head2": 4792,
        "tail2": 4796,
    },
    "slow_walk_speed": {
        "head": 1994,
        "tail": 1998,
        "head2": 4813,
        "tail2": 4817,
    },
    "soft_kick_speed": {
        "head": 2015,
        "tail": 2019,
        "head2": 4834,
        "tail2": 4838,
    },
    "soft_to_medium_kick_speed": {
        "head": 2046,
        "tail": 2050,
        "head2": 4865,
        "tail2": 4869,
    },
    "speed_scaler": {
        "head": 2064,
        "tail": 2068,
        "head2": 4883,
        "tail2": 4887,
    },
    "sprint_speed": {
        "head": 2082,
        "tail": 2086,
        "head2": 4901,
        "tail2": 4905,
    },
    "theoretical_max_acceleration": {
        "head": 2116,
        "tail": 2120,
        "head2": 4935,
        "tail2": 4939,
    },
    "theoretical_max_deceleration": {
        "head": 2150,
        "tail": 2154,
        "head2": 4969,
        "tail2": 4973,
    },
    "theoretical_max_diving_acceleration": {
        "head": 2191,
        "tail": 2195,
        "head2": 5010,
        "tail2": 5014,
    },
    "theoretical_max_diving_speed": {
        "head": 2225,
        "tail": 2229,
        "head2": 5044,
        "tail2": 5048,
    },
    "theoretical_max_potential_direction_change_jog": {
        "head": 2277,
        "tail": 2281,
        "head2": 5096,
        "tail2": 5100,
    },
    "theoretical_max_potential_direction_change_run": {
        "head": 2329,
        "tail": 2333,
        "head2": 5148,
        "tail2": 5152,
    },
    "theoretical_max_potential_direction_change_walk": {
        "head": 2382,
        "tail": 2386,
        "head2": 5201,
        "tail2": 5205,
    },
    "theoretical_max_running_speed": {
        "head": 2417,
        "tail": 2421,
        "head2": 5236,
        "tail2": 5240,
    },
    "theoretical_max_turning_rate": {
        "head": 2451,
        "tail": 2455,
        "head2": 5270,
        "tail2": 5274,
    },
    "theoretical_min_acceleration": {
        "head": 2485,
        "tail": 2489,
        "head2": 5304,
        "tail2": 5308,
    },
    "theoretical_min_deceleration": {
        "head": 2519,
        "tail": 2523,
        "head2": 5338,
        "tail2": 5342,
    },
    "theoretical_min_diving_acceleration": {
        "head": 2560,
        "tail": 2564,
        "head2": 5379,
        "tail2": 5383,
    },
    "theoretical_min_diving_speed": {
        "head": 2594,
        "tail": 2598,
        "head2": 5413,
        "tail2": 5417,
    },
    "theoretical_min_potential_direction_change_jog": {
        "head": 2646,
        "tail": 2650,
        "head2": 5465,
        "tail2": 5469,
    },
    "theoretical_min_potential_direction_change_run": {
        "head": 2698,
        "tail": 2702,
        "head2": 5517,
        "tail2": 5521,
    },
    "theoretical_min_potential_direction_change_walk": {
        "head": 2751,
        "tail": 2755,
        "head2": 5570,
        "tail2": 5574,
    },
    "top_speed": {
        "head": 2766,
        "tail": 2770,
        "head2": 5585,
        "tail2": 5589,
    },
    "very_hard_kick_speed": {
        "head": 2792,
        "tail": 2796,
        "head2": 5611,
        "tail2": 5615,
    },
    "very_slow_walk_speed": {
        "head": 2818,
        "tail": 2822,
        "head2": 5637,
        "tail2": 5641,
    },
    "walk_speed": {
        "head": 2834,
        "tail": 2838,
        "head2": 5653,
        "tail2": 5657,
    },
}


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


def load(file_name):
    with open(file_name, mode="rb") as file:
        file_content = file.read()

    data_all = []
    for i in range(len(file_content)):
        data = file_content[i : i + 1]
        data_all.append(data)

    return data_all


def save(data_all, save_name):
    save_byte = bytearray()
    for data in data_all:
        save_byte += data

    assert len(data_all) == len(save_byte), "length has to be fixed"

    with open(save_name, mode="wb") as file:
        file.write(save_byte)


def merge_hexadecimal(word):
    convert = "0x"
    for data in word:
        convert += f"{data:02x}"
    return int(convert, 16)


def split_hexadecimal(num, split_num=2):
    '''
    split_num : split hexadecimal by split_num
        ex ) x0004baf0 -> b'\x00', b'\x04', b'\xba', b'\xf0'
    '''
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


def convert(data_all, head, tail, update_value):
    before = get_word(data_all, head, tail)
    before = merge_hexadecimal(before)

    replaced = split_hexadecimal(update_value)
    replaced = replaced[-(tail - head):]
    for j, i in enumerate(range(tail, head, -1)):
        data_all[i] = replaced[j]

    after = get_word(data_all, head, tail)
    after = merge_hexadecimal(after)

    return before, after, data_all


def load_value(filename):
    with open(filename, "r") as rf:
        keys = json.load(rf)
    return keys


def notice(key, update_value, location):
    if key not in location:
        print(f"{key}는 FM24에 존재하지 않습니다")
        os.system('pause')
        sys.exit(-1)

    if key == "min_delay_for_shirt_tug_do":
        if update_value > 255 or update_value < 0:
            print(f"{key}의 범위는 0~255 사이여야 합니다")
            os.system('pause')
            sys.exit(-1)


def main(jsb_file, key_file):
    data_all = load(jsb_file)

    location = load_loacation()
    update_values = load_value(key_file)

    for key in update_values:
        update_value = update_values[key]
        notice(key, update_value, location)
        head1 = location[key]["head"]
        tail1 = location[key]["tail"]
        head2 = location[key]["head2"]
        tail2 = location[key]["tail2"]

        before, after, data_all = convert(data_all, head1, tail1, update_value)
        if before != after:
            print(key, before, "->", after)
        before, after, data_all = convert(data_all, head2, tail2, update_value)

    save(data_all, "physical_constraints_update.jsb")


if __name__ == "__main__":
    original_jsb = "physical_constraints.jsb"
    update_json = "physical_constraints.json"
    main(original_jsb, update_json)
    os.system('pause')
