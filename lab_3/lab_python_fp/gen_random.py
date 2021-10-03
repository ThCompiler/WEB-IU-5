import random

def gen_random(num_count, min, max):
    return [random.randint(min, max) for x in range(num_count)]