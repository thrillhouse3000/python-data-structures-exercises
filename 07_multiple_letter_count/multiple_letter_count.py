from unittest.util import _count_diff_all_purpose


def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counter = dict()
    for char in phrase:
        if counter.get(char):
            counter[char] += 1
        else:
            counter[char] = 1
    return counter