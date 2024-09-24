def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    int_c = 0 
    str_c = 0 

    for char in data:
        if char.isalpha():
            str_c += 1
        elif char.isdigit():
            int_c += 1
    return [str_c, int_c]
data = open("data/data05.txt", 'r').read()
print(main(data))
    
# Read data from file