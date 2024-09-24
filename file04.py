def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    i = 0
    ls = []
    while  i < len(data):
        if not data[i].isdigit():
            ls.append(data[i])
        i += 1
    return ls
data = open("data/data04.txt", 'r').read()
print(main(data))
# Read data from file