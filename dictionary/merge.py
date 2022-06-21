
def merge(main, addition):
    if addition is not None:
        addition_keys = list(addition.keys())[0]
        if addition_keys not in main:
            main[addition_keys] = 0
        main[addition_keys] = main[addition_keys] + addition[addition_keys]
        main['total_kills'] = main['total_kills'] + 1
