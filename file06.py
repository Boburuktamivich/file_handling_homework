def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a = data.splitlines()
    ls = []
    i = 0
    while i < len(a):
        ls.append(len(a[i]))
        i += 1
    return ls
data = open('data/data06.txt', 'r').read()
print(main(data))
# Read data from file