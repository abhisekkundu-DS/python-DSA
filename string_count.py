hash_list = [0]*27
abc = "abcdefghijklmnopqrstuvwxyzjjggfraaaaa"
def char_count(abc):
    global hash_list
    for i in abc:
        asci_value = ord(i)
        index = asci_value - 97
        hash_list[index] += 1
    return hash_list

ab = print(char_count(abc))

pqr = "abbc"
def char_count(pqr):
    global hash_list
    for i in pqr:
        asci_value = ord(i)
        index = asci_value - 97
        print(hash_list[index])

char_count(pqr)
