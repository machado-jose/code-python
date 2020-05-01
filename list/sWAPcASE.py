def swap_case(s):
    s_inverse = [x.upper() if x.islower() else x.lower() for x in s]
    return ''.join(s_inverse)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)