from dictionary.merge import merge
from extractors.killer_data_extractor import extract_deaths


def is_game_starter(text):
    return 'InitGame' in text


def is_game_end(text):
    return 'ShutdownGame' in text


def is_game_kill(text):
    return 'Kill' in text


def split_game_data(overall_dict, game_dict, lines):
    for line in lines:
        if is_game_starter(line):
            game_dict.clear()
            game_dict['total_kills'] = 0
        if is_game_end(line):
            overall_dict[len(overall_dict)+1] = game_dict.copy()
        if is_game_kill(line):
            merge(game_dict, extract_deaths(line))
