def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a = data.splitlines()
    ls = []
    i = 0
    while i < len(a):
        ls.append(len(a[i]))
        i += 1
    return max(ls)
data = open('data/data10.txt', 'r').read()
print(main(data))
# Read data from file