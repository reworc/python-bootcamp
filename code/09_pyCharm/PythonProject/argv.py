import sys

print(sys.argv[0])

if len(sys.argv) >= 2:
    for param in sys.argv[1:]:
        print(param)
