from unittest.mock import call

from printer.printer import print_killer_count, print_summary, print_killers_list


def test_should_print_just_killers_dictio(mocker):
    m = mocker.patch('builtins.print')
    dictio = {'total_kills': 0, 'leo': 1}
    print_killers_list(dictio)
    m.assert_called_once_with(['leo'])


def test_should_print_just_killers_dictio_empty(mocker):
    m = mocker.patch('builtins.print')
    dictio = {'total_kills': 0}
    print_killers_list(dictio)
    m.assert_called_once_with([])


def test_should_print_killers_and_count(mocker):
    m = mocker.patch('builtins.print')
    dictio = {'total_kills': 0, 'leo': 1}
    print_killer_count(dictio)
    m.assert_called_once_with('leo', 'has killed total of: ', '1')


def test_should_print_killers_and_count_empty(mocker):
    m = mocker.patch('builtins.print')
    dictio = {'total_kills': 0}
    print_killer_count(dictio)
    m.assert_not_called()


def test_should_print_summary(mocker):
    m = mocker.patch('builtins.print')
    dictio = {'total_kills': 0, 'leo': 1}
    print_summary(1, dictio)
    calls = [call('Game_1'),
             call('Summary'),
             call('Total of Kills: 0'),
             call('Killers:'),
             call(['leo']),
             call('leo', 'has killed total of: ', '1'),
             call('\n------------------------------\n')]
    m.assert_has_calls(calls)
