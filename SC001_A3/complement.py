"""
File: complement.py
Name: Leticia
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program finds the complement strand
    of a DNA sequence.
    """
    dna = 'ATC'
    print(build_complement(dna))
    dna = ''
    print(build_complement(dna))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    ans = ''
    if dna == '':
        return 'DNA strand is missing.'
    else:
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                ans += 'T'
            if ch == 'T':
                ans += 'A'
            if ch == 'C':
                ans += 'G'
            if ch == 'G':
                ans += 'C'
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
