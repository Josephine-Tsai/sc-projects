"""
File: similarity.py
Name: Josephine
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The user should give a long sequence of DNA and a short sequence of DNA.
    Then this program will turn all the letters into uppercase letters.
    After that, the program will use the dna_match function to match two dna strands.
    Finally find the most similar part and print it.
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    long_sequence = long_sequence. upper()
    short_sequence = input('What DNA sequence would you like to match? ')
    short_sequence = short_sequence. upper()
    ans = dna_match(long_sequence, short_sequence)
    print(ans)


def dna_match(long_sequence, short_sequence):
    """
    Find the part of long_sequence which is most similar with short_sequence.
    :param long_sequence: string, the combination of A, T, C, G.
    :param short_sequence: string, the combination of A, T, C, G.
    :return ans: string, the most similar part.
    """
    most_similar = 0
    place = 0
    for i in range(len(long_sequence) - len(short_sequence) + 1):
        count = 0
        for j in range(len(short_sequence)):
            # Record it if the dna is the same.
            if long_sequence[i+j] == short_sequence[j]:
                count += 1
        # Find most similar part and record its place.
        if count > most_similar:
            most_similar = count
            place = i
    ans = long_sequence[place: place+len(short_sequence)]
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
