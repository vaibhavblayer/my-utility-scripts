import sys

s = sys.argv[1]

bs = ''.join(format(ord(i), '08b') for i in s)
print(bs)
