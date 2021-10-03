from time import sleep
from lab_python_fp.field import field
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2
from lab_python_fp.gen_random import gen_random
from lab_python_fp.uniq import Unique
import lab_python_fp.sorted

def test_field():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    result = field(goods, 'title')
    print(result)
    result = field(goods, 'title', 'price')
    print(result)

def test_gen_random():
    print(gen_random(5, 1, 4))

def test_uniq():
    uniq = Unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
    print([x for x in uniq])
    
    uniq = Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'], ignore_case=True)
    print([x for x in uniq])
    
    uniq = Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'])
    print([x for x in uniq])
    
def test_timer():
    with cm_timer_1():
        sleep(5.5)
        
    with cm_timer_1():
        sleep(3.6)
    
def main():
   test_field()
   test_gen_random()
   test_uniq()
   test_timer()

if __name__ == "__main__":
    main()