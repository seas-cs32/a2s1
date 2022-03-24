'''
cmp_strmatch.py compares the brute-force and Rabin-Karp string-matching
algorithms across a range of input text and pattern sizes.
'''

import sys
import time
from bf_strmatch import bf_strmatch
from rk_strmatch import rk_strmatch

def compare_times(t, p):
    print(f'For p = {len(p)} bytes, t = {len(t)} bytes')

    start = time.process_time()
    bf_strmatch(t, p)
    print(f'bf_strmatch took {time.process_time() - start} secs')

    start = time.process_time()
    rk_strmatch(t, p)
    print(f'rk_strmatch took {time.process_time() - start} secs')

    print('')

def main():
    # Check for proper usage and grab the input strings
    if len(sys.argv) != 1:
        sys.exit("Usage: python3 cmp_strmatch.py")

    # Grab the text from a file
    with open('JustDavid.txt') as f:
        t_orig = f.read()

    # A reasonable search pattern that won't ever match.  The loop grows it
    # through repetition to be about a quarter the size of the text input.
    p_orig = 'David laughed softty'
    p_big = p_orig
    while len(p_big) < len(t_orig) // 4:
        p_big += p_big

    times_to_double = 7

    print('### Test: m << t')
    t = t_orig
    p = p_orig
    for i in range(times_to_double):
        compare_times(t, p)
        t += t
        p += p

    print('### Test: m < t')
    t = t_orig
    p = p_big
    for i in range(times_to_double):
        compare_times(t, p)
        t += t
        p += p

if __name__ == '__main__':
    main()
