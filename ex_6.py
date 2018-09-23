import json
import random
from ex_4 import print_result
from ex_5 import Main


path = 'data_light.json'

with open(path) as file:
    data = json.load(file, encoding="utf-8")

@print_result
def f1(arg):
    return sorted(list(set([data[prof_el]["job-name"].lower() for prof_el in range(len(data))])))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("программист"), arg))


@print_result
def f3(arg):
    return [i + " с опытом Python" for i in arg]


@print_result
def f4(arg):
    money = [random.randrange(100000, 200000) for i in range(len(arg))]
    return ["{}, зарплата {}".format(x, y) for x, y in zip(arg, money)]


with Main():
    f4(f3(f2(f1(data))))