from dictionary.merge import merge


def test_should_add_new_key_when_not_exists():
    overall_dict = {'total_kills': 0}
    game_dict = {'sady': 1}
    merge(overall_dict, game_dict)
    assert overall_dict['total_kills'] == 1
    assert overall_dict['sady'] == 1


def test_should_add_new_key_when_already_exists():
    overall_dict = {'total_kills': 1, 'sady': 1}
    game_dict = {'sady': 1}
    merge(overall_dict, game_dict)
    assert overall_dict['total_kills'] == 2
    assert overall_dict['sady'] == 2


def test_should_increase_total_count():
    overall_dict = {'total_kills': 1, 'sady': 1}
    game_dict = {'leo': 1}
    merge(overall_dict, game_dict)
    assert overall_dict['total_kills'] == 2
    assert overall_dict['sady'] == 1
    assert overall_dict['leo'] == 1


def test_should_not_fail_when_there_is_no_kill_at_game():
    overall_dict = {'total_kills': 1, 'sady': 1}
    game_dict = None
    merge(overall_dict, game_dict)
    assert overall_dict['total_kills'] == 1
    assert overall_dict['sady'] == 1

