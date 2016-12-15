# encoding: utf-8
import sys

# stats: 能力值
# base: 种族值
# effort: 努力
# nature: 性格
# individual: 个体

def get_hp_stats(base, effort_add):
    return (base * 2 + 31 + effort_add) * 0.5 + 10 + 50

def get_stats(base, effort_add, nature_admend, individual_value = 31):
    return int(((base * 2 + individual_value + effort_add) * 0.5 + 5) * nature_admend)

def get_stats_complete(base):
    # min0: extreme low, used for low speed in trick room
    min0 = get_stats(base, 0, 0.9, 0)
    min1 = get_stats(base, 0, 1.0)
    max0 = get_stats(base, 63, 1.0)
    max1 = get_stats(base, 63, 1.1)
    return [("min-", min0), ("min", min1), ("max", max0), ("max+", max1)]

def get_base(stats):
    return int(((stats / 1.1 - 5) * 2 - 94) / 2)

def main():
    print get_stats_complete(100)
    print get_base(184)
    print get_hp_stats(70, 63)

if __name__ == '__main__':
    main()