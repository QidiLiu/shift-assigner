
def addSpace(in_str):
    """
    @brief Add spaces to the end of a string to make windows looks better
    @param in_str The string
    """
    out_sum = 13
    return in_str + '　' * (out_sum - len(in_str)) + '  '