from selectors import EpollSelector


def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # set_nums = set(nums)
    # mode = 0

    # for num in set_nums:
    #     if nums.count(num) > mode:
    #         mode = num
    # return mode
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    max_value = max(counter.values())

    for (num, count) in counter.items():
        if count == max_value:
            return num