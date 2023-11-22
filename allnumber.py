def print_formatted(number):
    width = len("{0:b}".format(number))  # Calculate width based on binary representation of the number
    
    for i in range(1, number + 1):
        decimal = "{0:{width}d}".format(i, width=width)
        octal = "{0:{width}o}".format(i, width=width)
        hexadecimal = "{0:{width}X}".format(i, width=width)
        binary = "{0:{width}b}".format(i, width=width)
        
        print(f"{decimal} {octal} {hexadecimal} {binary}")

# Example usage:
num = 10  # Replace this number with any desired value
print_formatted(num)
