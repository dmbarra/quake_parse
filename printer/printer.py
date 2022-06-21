
def print_killers_list(dict):
    dict.pop('total_kills')
    print(list(dict.keys()))


def print_killer_count(dict):
    dict.pop('total_kills')
    for killer in dict:
        print(str(killer), 'has killed total of: ', str(dict[killer]))


def print_summary(key, dict):
    print('Game_' + str(key))
    print('Summary')
    print('Total of Kills: ' + str(dict['total_kills']))
    print('Killers:')
    print_killers_list(dict.copy())
    print_killer_count(dict.copy())

    print('\n------------------------------\n')
