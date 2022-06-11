from curses.ascii import NUL
from ntpath import join
import sys

def main():
    t = sys.argv[1:]
    s = ' '.join(t)
    if not s:
        return (0);
    s = s[::-1]
    i = 0;
    while i < len(s):
        if (s[i] >= 'A' and s[i] <= 'Z'):
            print(chr(ord(s[i])+32), end='')
        elif (s[i] >= 'a' and s[i] <= 'z'):
          print(chr(ord(s[i])-32), end='')
        else:
            print(s[i], end='')
        i += 1
main()
