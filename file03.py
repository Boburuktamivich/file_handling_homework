def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    i = 0
    ls = []
    while i < len(data):
        if data[i].isdigit():
            ls.append(data[i])
        i += 1
    return ls
data = open("data/data03.txt", 'r').read()
print(main(data))