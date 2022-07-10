import string

def print_rangoli(size):
    
    # your code goes here
    alpha = string.ascii_lowercase
    
    temp = "-".join(alpha[0:size])
    width = len((temp[::-1]+temp[1:]))

    result = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        result.append((s[::-1]+s[1:]).center(width, "-"))
    print('\n'.join(result[:0:-1]+result))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)