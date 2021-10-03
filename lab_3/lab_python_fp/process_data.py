import json
import sys
from field import field
from cm_timer import cm_timer_1, cm_timer_2
from gen_random import gen_random
from uniq import Unique
from print_result import print_result

path = 'data_light.json'

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith(('программист', 'Программист')), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list(map(lambda x: ''.join(x), list(zip(arg, [', зарплата ' + str(x) + ' руб.' for x in gen_random(len(arg), 100000, 200000)]))))


if __name__ == '__main__':
    with open(path) as f:
        data = json.load(f)
        
    with cm_timer_1():
        f4(f3(f2(f1(data))))