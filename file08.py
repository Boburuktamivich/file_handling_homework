def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
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
    return max(ls)  
data = open("data/data08.txt", 'r').read()
print(main(data))


# Read data from file