ALPHABET = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
print('Your alphabet is:', ALPHABET)
print('Length:', len(ALPHABET))

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        code = ALPHABET.find(letter)
        code += key
        ciphertext += ALPHABET[code%len(ALPHABET)]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        code = ALPHABET.find(letter)
        code -= key
        plaintext += ALPHABET[code%len(ALPHABET)]
    return plaintext

mode = ''
while mode != 'q':
    mode = input('Enter mode (e/d/q): ')
    if mode == 'e':
        plaintext = input('Enter plaintext: ')
        key = int(input('Enter key: '))
        ciphertext = encrypt(plaintext, key)
    elif mode == 'd':
        ciphertext = input('Enter ciphertext: ')
        key = int(input('Enter key: '))
        plaintext = decrypt(ciphertext, key)
    elif mode == 'q':
        continue
    else:
        print('Unknown mode')
        continue
    print(' Plaintext:', plaintext)
    print('Ciphertext:', ciphertext)
print('Thank you for using the Caesar cipher')
