def print_pretty_table(data, cell_sep=' | ', header_separator=True):
    rows = len(data)
    cols = len(data[0])
    col_width = []
    
    for col in range(cols):
        columns = [str(data[row][col]) for row in range(rows)]
        col_width.append(len(max(columns, key=len)))
    
    separator = "-+-".join('-' * n for n in col_width)
    for i, row in enumerate(range(rows)):
        if i == 1 and header_separator:
            print(separator)
        
        result = []
        for col in range(cols):
            item = str(data[row][col]).rjust(col_width[col])
            result.append(item)
        print(cell_sep.join(result))
        

max_int = 10000000000000000000000000000000000

def change_elem(x, new_val, id):
    x[id] = new_val
    return x