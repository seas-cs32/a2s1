import sys
import re
import string

# Instead of bothering to ask the user for this information on each run of the
# program, we'll just make them global constants.  In production code, we'd
# define this information in a configuration file, which would be a better way
# to have our user infrequently change what are relatively stable constants than
# asking this user to edit our scripts.
MIN_LEN = 4           # don't index any words shorter than 5 chars
UNIT_PAT = ''         # for pages in CatInTheHat.txt
UNIT_CNT_INIT = 1
'''
UNIT_PAT = 'CHAPTER'  # for chapters in JustDavid.txt
UNIT_CNT_INIT = 0
'''

def get_wordlist(line):
    """ The magic function that turns a line into a wordlist"""
    line = line.replace('--', ' ')
    return [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w)
            for w in line.split()]

# An unfortunately difficult check because of empty lines as
# a unit break in CatInTheHat.txt
def found_new_unit(line):
    if UNIT_PAT == '':
        return UNIT_PAT == line
    else:
        return UNIT_PAT == line[0:len(UNIT_PAT)]

def update_index(d, wordlist, unitno):
    for word in wordlist:
        # Skip short words
        if len(word) < MIN_LEN:
            continue
        
        # No capitals
        word = word.lower()

        # Update our dictionary
        if word in d:
            if unitno not in d[word]:
                d[word].append(unitno)
        else:
            d[word] = [unitno]

    return d

def build_index(txt):
    # Start with an empty dictionary
    d = {}

    # Iterate through each line in book watching for book unit boundaries
    unitno = UNIT_CNT_INIT
    for line in txt.split('\n'):
        if found_new_unit(line):
            unitno += 1
        else:
            d = update_index(d, get_wordlist(line), unitno)

    # Print out the index
    for w in sorted(d):
        pages = str(d[w]).strip('[]')
        print(f'{w}: {pages}')

def main():
    # Check for proper usage and grab the input strings
    if len(sys.argv) == 1:
        txt = sys.stdin.read()
    elif len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            txt = f.read()
    else:
        print("Usage: python3 buildindex.py book.txt")
        print("   Or: python3 buildindex.py < book.txt")
        sys.exit()

    build_index(txt)

if __name__ == '__main__':
    main()
