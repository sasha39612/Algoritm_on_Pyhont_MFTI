objects = []
def foo(x):
    print('foo', x)

def bar(a, b):
    """ Эта функция складывает и возвращает сумму
    """
    return a + b

def create_object(name):
    objects.append("object[" + name + "]")

def print_objects():
    print("Все дбавленные объекты:")
    for obj in objects:
        print(obj)

if __name__ == '__main__':
    print('Library executed separately.')
    print("Let's test itself")
    if bar(2, 2) == 4:
        print("OK")
    else:
        print("FAIL")

