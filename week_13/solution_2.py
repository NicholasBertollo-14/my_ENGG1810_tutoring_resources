
def mode(values: list[float]) -> set[float]:
    """
    Returns the mode/modes of the data set. 
    E.g. [1, 2, 3, 4, 5, 6, 5, 5, 4, 3, 2, 3, 4, 4, 4, 4, 4] -> {4}
    If the data set is empty then throw a ValueError
    If the data set has multiple
    """
    if len(values) == 0:
        raise ValueError
    frequency: dict[float: int] = {}
    for value in values:
        if value in frequency.keys():
            frequency[value] += 1
        else:
            frequency[value] = 1
    
    modes: set[float] = set()
    amount_of_the_modes: int = 0
    for value, amount in frequency.items():
        if amount > amount_of_the_modes:
            modes = {value}
            amount_of_the_modes = amount
        elif amount == amount_of_the_modes:
            modes.add(value)
    return modes

def median(values: list[float]) -> float:
    """
    Returns the median of the data set.
    E.g. [4, 5, 2, 3, 1] -> 3
    If the list is empty then throw a ValueError
    Note: To sort a list use the .sort() method on the list.
    """
    if len(values) == 0:
        raise ValueError("Cannot find the median of an empty list")
    values.sort()
    middle_index: int = len(values) // 2 # High school formula assume 1-index
    if len(values) % 2 == 0:
        # If even then middle_index is right middle index
        # take average in this case. 
        return (values[middle_index] + values[middle_index - 1]) / 2
    else:
        return values[middle_index]

def five_figure_summary(values: list[float]) -> list[float]:
    """
    Returns the five figure summary. 
    This includes, in order:
        The minimum
        The first quartile
        The median
        The third quartile
        The maximum
    You can use built in functions. 
    If the list has less than 3 numbers then raise a ValueError
    E.g. [1, 2, 3] -> [1, 1, 2, 3, 3]
    Note: To sort a list use the .sort() method 
    """
    if len(values) < 3:
        raise ValueError("Cannot find five figure summary of an empty list!")
    summary: list[float] = [min(values)]
    middle_index: int = len(values) // 2
    summary.append(median(values[:middle_index]))
    summary.append(median(values))
    if len(values) % 2 == 0:
        summary.append(median(values[middle_index:]))
    else:
        summary.append(median(values[middle_index + 1:]))
    summary.append(max())
    return summary # This is probably wrong due to an off by 1 error.
