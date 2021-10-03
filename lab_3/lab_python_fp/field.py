

def field(items, *args):
    assert len(args) > 0
    result = []
    
    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item:
                result.append(item[key])
    else:
        for item in items:
            result.append({key: value for key, value in item.items() if key in args})
    return result

