def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    return data.split(",")
data = open("data/data01.txt", "r").read()
print(main(data))

# Read data from file