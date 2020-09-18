"""
File: complement.py
Name: Josephine
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    The user should give a DNA strand(A, T, C, G).
    And this program will turn all the letters into uppercase letters.
    Then give back the complement of the DNA strand.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna = dna. upper()
    ans = complement(dna)
    print('The complement of ' + dna + ' is ' + ans)


def complement(dna):
    """
    Turn 'A' to 'T', and 'T' to 'A'. Turn 'C' to 'G', and turn 'G' to 'C'.
    :param dna: string, the combination of A, T, C, G.
    :return ans: string, the complement of the dna.
    """
    ans = ''
    for i in dna:
        if i == 'A':
            ans += 'T'
        elif i == 'T':
            ans += 'A'
        elif i == 'G':
            ans += 'C'
        else:
            ans += 'G'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
