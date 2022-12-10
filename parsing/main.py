import sys

# Usage: main.py {FILENAME}

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write(message)


# processing the argument vector
print(sys.argv)