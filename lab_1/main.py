import sys
import math

def force_conv_number(string):
    try:
        return float(string)
    except:
        return None

def _get_coef(index, prompt):
    coef_str = ''
    if len(sys.argv) > index:
        coef_str = sys.argv[index]
    else:
        print(prompt)
        coef_str = input()
        
    return force_conv_number(coef_str)

def get_coef(index, prompt):
    tmp = None
    while tmp == None:
        tmp = _get_coef(index, prompt)
    return tmp


def complex_sqrt(number):
    return pow(number, 0.5)


def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    sqD = complex_sqrt(complex(D, 0))
    root1 = (-b + sqD) / (2.0*a)
    root2 = (-b - sqD) / (2.0*a)
    
    result.append(complex_sqrt(root1))
    result.append(-complex_sqrt(root1))
    result.append(complex_sqrt(root2))
    result.append(-complex_sqrt(root2))
    return result


def print_roots(roots):
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыри корня: {} и {}'.format(roots[0], roots[1], roots[3], roots[4]))


def input_coef():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    
    return [a, b, c]


def main():
    [a, b, c] = input_coef()
    
    roots = get_roots(a,b,c)

    real_roots = list(map(lambda x: x.real, filter(lambda number: number.imag == 0, roots)))
    
    print_roots(real_roots)


if __name__ == "__main__":
    main()
