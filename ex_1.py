import random


def gen_random(min, max, count):
    for num in range(count):
        yield random.randrange(min,max+1)


def field(list, *args):
    for el in list:
        if len(args) == 0:
            return None
        elif len(args) == 1:
            if args[0] in el.keys():
                if el[args[0]] is not None:
                    yield el[args[0]]
        else:
            res = {}
            for arg in args:
                if arg in el.keys():
                    if el[arg] is not None:
                        res[arg] = el[arg]
            if res:
                yield res

def main():
    list = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    print([i for i in field(list, 'color')])

    print([i for i in gen_random(1,10,5)])


if __name__ == "__main__":
    main()