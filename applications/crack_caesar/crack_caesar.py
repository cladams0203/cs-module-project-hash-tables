# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open('ciphertext.txt') as f:
    cipher = f.read()

def decode_cipher():
    count = {}
    commons = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    s = list(cipher)
    for i in s:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    sorted_dictionary = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    stripped_dictionary = {k:v for (k,v) in sorted_dictionary.items() if k in commons}
    stripped_array = []
    for i in stripped_dictionary:
        stripped_array.append(i)
    decoder = {}
    for idx, val in enumerate(stripped_array):
        decoder[val] = commons[idx]
    for idx, val in enumerate(s):
        if val in decoder:
            s[idx] = decoder[val]
    return ''.join(s)














print(decode_cipher())