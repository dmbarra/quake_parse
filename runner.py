import sys

print('File path', sys.argv[1])
file_path = sys.argv[1]

with open(file_path) as f:
    lines = f.readlines()

for line in lines:
    print(line)
