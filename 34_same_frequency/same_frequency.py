def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    counter1 = {}
    n_str1 = str(num1)
    n_str2 = str(num2)
    for n in n_str1:
        counter1[n] = counter1.get(n, 0) + 1
    counter2 = {}
    for n in n_str2:
        counter2[n] = counter2.get(n, 0) + 1
    
    return True if counter1 == counter2 else False
