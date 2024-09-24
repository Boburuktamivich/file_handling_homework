def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return len(data)
data = open("data/data02.txt", 'r').read()
print(main(data))
# Read data from file