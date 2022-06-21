from extractors.killer_data_extractor import is_killed_by_world, is_killed_by_another_player, extract_death_for_world, \
    extract_player_kill, extract_deaths


def test_should_confirm_that_is_kill_from_world():
    text = '20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT'
    assert is_killed_by_world(text)


def test_should_not_confirm_that_is_kill_from_world():
    text = '22:40 Kill: 2 2 7: Isgalamido killed Isgalamido by MOD_ROCKET_SPLASH'
    assert not is_killed_by_world(text)


def test_should_confirm_that_is_kill_from_another_player():
    text = '22:40 Kill: 2 2 7: Isgalamido killed Isgalamido by MOD_ROCKET_SPLASH'
    assert is_killed_by_another_player(text)


def test_should_not_confirm_that_is_kill_another_player():
    text = '20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT'
    assert not is_killed_by_another_player(text)


def test_should_return_as_death_when_world_killed_him_and_his_name():
    text = '20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT'
    result = extract_death_for_world(text)
    assert result['Isgalamido'] == -1


def test_should_return_the_killer_name_and_count():
    text = '22:40 Kill: 2 2 7: Isgalamido killed sady by MOD_ROCKET_SPLASH'
    result = extract_player_kill(text)
    assert result['Isgalamido'] == 1


def test_should_select_and_return_as_death_when_world_killed_him_and_his_name():
    text = '20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT'
    result = extract_deaths(text)
    assert result['Isgalamido'] == -1


def test_should_select_and_return_the_killer_name_and_count():
    text = '22:40 Kill: 2 2 7: Isgalamido killed sady by MOD_ROCKET_SPLASH'
    result = extract_deaths(text)
    assert result['Isgalamido'] == 1
