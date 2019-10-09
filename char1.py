def recchar(charstr):
    hash_hd = []
    for char in charstr:
        if char not in hash_hd:
            hash_hd.append(str(char))
        else:
            print(hash_hd)
            return char
    print(hash_hd)
    return None

if __name__ == '__main__':
    print(recchar(str(input('Input a string '))))
