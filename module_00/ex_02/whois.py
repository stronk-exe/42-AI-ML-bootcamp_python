import sys

def main():
    if len(sys.argv) != 2:
        print('Invalid input')
        exit(1);
    if not (sys.argv[1]).isnumeric():
        print('Invalid input')
        exit(1);
    n = int(sys.argv[1])
    if not n:
        print("I'm Zero.")
    elif not (n % 2):
        print("I'm Even.")
    elif (n%2):
        print("I'm Odd.")
main()