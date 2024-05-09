def get_not_empty_tuples(lst):
   return [tp for tp in lst if len(tp) >0 and set(tp) != {''}]


def replace_to_python(lst):
    return [tuple(list(tp[:2])+['Python']) for tp in lst]


if __name__ == '__main__':
    tuples1 = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
    tuples2 = [("Программирую","на", "языке", "Swift"), ("Программирую","на", "языке", "R"),("Программирую","на", "языке", "C++"),("Программирую","на", "языке", "JavaScript")]
    print(get_not_empty_tuples(tuples1))
    print(replace_to_python(tuples2))
