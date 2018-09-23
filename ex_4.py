def print_result(func):
    def main(arg):
        print(func.__name__)
        funcRes = func(arg)

        if isinstance(funcRes, list):
            print('\n'.join([str(i) for i in funcRes]))
        elif isinstance(funcRes, dict):
            print('\n'.join(["{} = {}".format(key, value) for key, value in funcRes.items()]))
        return funcRes

    return main


if __name__ == '__main__':
    @print_result
    def test_1(arg):
        return 1


    @print_result
    def test_2(arg):
        return 'iu'


    @print_result
    def test_3(arg):
        return {'a': 1, 'b': 2}


    @print_result
    def test_4(arg):
        return [1, 2]


    test_1(1)
    test_2(1)
    test_3(1)
    test_4(1)
