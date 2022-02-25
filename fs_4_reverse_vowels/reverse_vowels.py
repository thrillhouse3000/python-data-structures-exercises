def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    r_vowels = [char for char in s if char in vowels]
    r_vowels.reverse()
    new_str = ''
    
    for ltr in s:
        if ltr in vowels:
            new_str += r_vowels[0]
            r_vowels.pop(0)
        else:
            new_str += ltr
    return new_str