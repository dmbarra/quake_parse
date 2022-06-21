import sys

from extractors.game_data_extractor import split_game_data

overall_dict = {}
game_dict = {}

print('File path', sys.argv[1])
file_path = sys.argv[1]

with open(file_path) as f:
    lines = f.readlines()

split_game_data(overall_dict, game_dict, lines)

print(len(overall_dict))
