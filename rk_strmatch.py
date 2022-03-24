'''
rk_strmatch.py implements the Rabin-Karp string-matching algorithm.

To watch the algorithm in action, you can remove the comment characters at the
start of the 5 DEBUG print statements, and the else-statement protecting the
count of hash collisions.  If you're running with a large input text string,
I recommend keeping the comment character on lines 38 and 56, which will show
you only the hash collisions.
'''

import sys

def rk_strmatch(t, p):
    n = len(t)
    m = len(p)

    # Preprocessing steps

    # Constants in Rabin-Karp string-matching problem
    d = 256    # number of character encodings in ASCII
    q = 65537  # a prime number

    # Compute the hash value of a 1 in the high-order position (i.e.,
    # m-1th position), where digits have radix d
    hh = 1
    for i in range(m - 1):
        hh = (hh * d) % q

    # Calculate the hash values for p and t[0:m], since the matching
    # loop needs these values as it starts
    hp = 0
    ht = 0
    for i in range(m):
        hp = ((hp * d) + ord(p[i])) % q
        ht = ((ht * d) + ord(t[i])) % q

    #print(f'DEBUG: pattern hash("{p[0:m]}") = {hp}')
    #print(f'DEBUG: hash("{t[0:m]}") = {ht}')

    # Matching step
    for s in range(n - m + 1):
        if hp == ht:
            # Verify that this is an actual match
            if p[0:m] == t[s:s+m]:
                print(f'Pattern occurs with shift {s}')
            #else:
                #print(f'DEBUG: hash collision')
                #print(f'DEBUG: hash("{t[s:s+m]}") = {ht}')

        if s < n - m:
            # Need to compute hash for next iteration
            ht = ((ht - (ord(t[s]) * hh)) * d
                  + ord(t[s+m])) % q
            if ht < 0:
                ht += q
            #print(f'DEBUG: hash("{t[s+1:s+1+m]}") = {ht}')

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
        sys.exit("Usage: python3 rk_strmatch.py text pattern")

    rk_strmatch(t, p)

if __name__ == '__main__':
    main()
