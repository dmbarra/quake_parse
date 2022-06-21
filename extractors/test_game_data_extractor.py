from extractors.game_data_extractor import is_game_starter, is_game_end, split_game_data, is_game_kill


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


def test_should_confirm_that_is_a_kill():
    text = '23:06 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT'
    assert is_game_kill(text)


def test_should_not_confirm_that_is_a_kill():
    text = 'lientUserinfoChanged: 2 nIsgalamidomodel'
    assert not is_game_kill(text)


def test_should_add_game_and_kills():
    overall_dict = {}
    game_dict = {}
    lines = """  0:00 InitGame: xasdasdasdasd \n
                15:00 Exit: Timelimit hit. \n
                20:34 ClientConnect: 2 \n
                20:54 Kill: 1022 2 22: <world> killed leo by MOD_TRIGGER_HURT \n
                20:34 ClientUserinfoChanged: 2 asdasdasdasd \n
                20:37 ClientUserinfoChanged: 2 asdasdasdad \n
                20:37 ClientBegin: 2 \n
                20:37 ShutdownGame: \n
            """.split('\n')
    split_game_data(overall_dict, game_dict, lines)
    assert len(overall_dict) == 1
    assert overall_dict[1]['total_kills'] == 1
    assert overall_dict[1]['leo'] == -1


def test_should_add_game_and_kills_for_multi_games():
    overall_dict = {}
    game_dict = {}
    lines = """  0:00 InitGame: xasdasdasdasd \n
                15:00 Exit: Timelimit hit. \n
                20:34 ClientConnect: 2 \n
                20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT \n
                20:34 ClientUserinfoChanged: 2 asdasdasdasd \n
                20:37 ClientUserinfoChanged: 2 asdasdasdad \n
                20:37 ClientBegin: 2 \n
                20:37 ShutdownGame: \n
                
                0:00 InitGame: xasdasdasdasd \n
                15:00 Exit: Timelimit hit. \n
                20:34 ClientConnect: 2 \n
                22:06 Kill: 2 3 7: Isgalamido killed Mocinha by MOD_ROCKET_SPLASH \n
                20:34 ClientUserinfoChanged: 2 asdasdasdasd \n
                20:37 ClientUserinfoChanged: 2 asdasdasdad \n
                20:37 ClientBegin: 2 \n
                20:37 ShutdownGame: \n
            """.split('\n')
    split_game_data(overall_dict, game_dict, lines)
    assert len(overall_dict) == 2
    assert overall_dict[1]['total_kills'] == 1
    assert overall_dict[1]['Isgalamido'] == -1
    assert len(overall_dict) == 2
    assert overall_dict[2]['total_kills'] == 1
    assert overall_dict[2]['Isgalamido'] == 1
