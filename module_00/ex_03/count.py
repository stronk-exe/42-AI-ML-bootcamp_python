import sys

def text_analyzer(t):
    # t = sys.argv[1:]
    i = 0
    u = 0
    l = 0
    s = 0
    while (t[i] != '\0'):
        if t[i] >= 'a' and t[i] <= 'z':
            l+=1
        elif t[i] >= 'A' and t[i] <= 'Z':
            u+=1
        elif t[i] == ' ':
            s+=1
        i+=1
    print(u + ' upper letter(s)')
    print(l + ' lower letter(s)')
    print(s + ' space(s)')

text_analyzer('gg')