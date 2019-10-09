def sumhash(inp, sum):
    hashTable = []
    for i in inp:
        if i in hashTable:
            print(True)
            print(i, sum - i)
            print(hashTable)
            return True
        else:
            hashTable.append(sum - i)
    print(False)
    print(hashTable)
    return False


if __name__ == '__main__':
      input1 = [1, 2, 4, 9]
      input2 = [1, 2, 4, 6, 4]
      input3 = []
      input4 = [-1, 2, 3, 4, 9]
      sum    = 8
      sumhash(input1, sum)
      sumhash(input2, sum)
      sumhash(input3, sum)
      sumhash(input4, sum)
