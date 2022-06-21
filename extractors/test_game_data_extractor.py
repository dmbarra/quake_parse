from extractors.game_data_extractor import is_game_starter, is_game_end, split_game_data


def test_should_confirm_that_is_a_starter():
    text = '0:00 InitGame: v_floodProtectsv_maxPingv_minPingv_ma'
    assert is_game_starter(text)


def test_should_not_confirm_that_is_a_starter():
    text = 'lientUserinfoChanged: 2 nIsgalamidomodel'
    assert not is_game_starter(text)


def test_should_confirm_that_is_a_end():
    text = '20:37 ShutdownGame:'
    assert is_game_end(text)


def test_should_not_confirm_that_is_a_end():
    text = 'lientUserinfoChanged: 2 nIsgalamidomodel'
    assert not is_game_end(text)


def test_should_add_game_into_dictionary():
    overall_dict = {}
    game_dict = {}
    lines = """  0:00 InitGame: xasdasdasdasd \n
                15:00 Exit: Timelimit hit. \n
                20:34 ClientConnect: 2 \n
                20:34 ClientUserinfoChanged: 2 asdasdasdasd \n
                20:37 ClientUserinfoChanged: 2 asdasdasdad \n
                20:37 ClientBegin: 2 \n
                20:37 ShutdownGame: \n
            """.split('\n')
    split_game_data(overall_dict, game_dict, lines)
    assert len(overall_dict) == 1
    assert game_dict['total_kills'] == 0
