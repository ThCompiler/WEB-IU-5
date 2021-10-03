
class Unique(object):
    def __init__(self, items, **kwargs):
        self.checked = []
        self.iter = iter(items)
        
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False
            
        pass

    def __next__(self):
        current_element = next(self.iter)
        while True:
            stop_for = True
            for element in self.checked:
                if self.ignore_case:
                    try:
                        stop_for = not (element.lower() == current_element.lower())
                    except:
                        stop_for = not (element == current_element)
                else:
                    stop_for = not (element == current_element)
                if not stop_for:
                    break
                
            if stop_for:
                break
            else:
                current_element = next(self.iter)

        self.checked.append(current_element)
        return current_element

    def __iter__(self):
        return self