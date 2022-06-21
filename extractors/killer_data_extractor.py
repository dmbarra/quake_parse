def is_killed_by_world(text):
    return '<world> killed' in text


def is_killed_by_another_player(text):
    return 'killed' in text and '<world> killed' not in text


def extract_death_for_world(text):
    left = '<world> killed '
    right = ' by '
    return {text[text.index(left) + len(left):text.index(right)].strip(): -1}


def extract_player_kill(text):
    left = ': '
    right = ' killed '
    return {text[text.index(left) + len(left):text.index(right)].split(':')[1].strip(): 1}


def extract_deaths(text):
    if is_killed_by_world(text):
        return extract_death_for_world(text)
    if is_killed_by_another_player(text):
        return extract_player_kill(text)
