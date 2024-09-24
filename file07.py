def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    i = 0
    c = 0
    while i < len(data):
        if data[i].isdigit():
            c += int(data[i])
        i += 1
    return c

data = open("data/data07.txt", 'r').read()
print(main(data))
# Read data from file