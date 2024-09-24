def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    i = 0
    ls = []

    while i < len(data):
        if data[i].isdigit():
            ls.append(data[i])
        i += 1
    return min(ls)
data = open("data/data09.txt", "r").read()
print(main(data))

# Read data from file