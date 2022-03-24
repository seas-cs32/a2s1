'''
bf_strmatch.py is another Python implementation of our brute-force
string-matching algorithm.
'''

import sys

def bf_strmatch2(t, p):
    n = len(t)
    m = len(p)
    for s in range(n - m + 1):
        for i in range(m):
            if p[i] != t[s+i]:
                break
        else:
            print(f'Pattern occurs with shift {s}')

def main():
    # Check for proper usage and grab the input strings
    if len(sys.argv) == 1:
        t = input('Text: ')
        p = input('Pattern: ')
    elif len(sys.argv) == 2:
        # Reads text from stdin
        t = sys.stdin.read()
        p = sys.argv[1]
    elif len(sys.argv) == 3:
        t = sys.argv[1]
        p = sys.argv[2]
    else:
        sys.exit("Usage: python3 bf_strmatch2.py text pattern")

    bf_strmatch2(t, p)

if __name__ == '__main__':
    main()
