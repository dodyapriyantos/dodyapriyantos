def print_formatted(number):
    # your code goes here
    LenOfDigit = len(str(bin(number).lstrip("0b")))
    for i in range (1, number+1):
        print ( str(i).rjust(LenOfDigit, " ") + str(oct(i)).lstrip("0o").rjust(LenOfDigit+1, " ") + str(hex(i)).lstrip("0x").rjust(LenOfDigit+1, " ").upper() + str(bin(i)).lstrip("0b").rjust(LenOfDigit+1, " "))
    
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)