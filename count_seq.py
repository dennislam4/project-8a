# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 11-14-2022
# Description: Generator function generates number sequence from generator object. The sequence is yielded as terms in
# the form of a string. The sequence is seperated by 1's that are counted within the generator sequence.

def count_seq():
    """
    Generator function that generates number sequence string. The sequence counts the numbers of each digit for each
    iteration of the sequences.
    """

    num = "2"
    yield num

    while num:
        length = len(num)
        val = 0
        sequence = ""

        for element in range(0, length):
            val += 1

            if length <= element + 1 or num[element + 1] != num[element]:
                sequence += str(val)
                sequence += num[element]
                val = 0

            else:
                pass
        num = sequence
        yield num
