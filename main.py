import itertools

def decrypt(ciphertext, key):
    """
    Decrypt the given ciphertext using the provided key.
    """
    plaintext = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_dict = {key[i]: alphabet[i] for i in range(len(alphabet))}  
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = key_dict.get(char.upper(), char)
            if char.islower():
                decrypted_char = decrypted_char.lower()
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)  
    return ''.join(plaintext)

def brute_force_decrypt(ciphertext):
    """
    Try all possible permutations of the alphabet to decrypt the ciphertext.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_keys = itertools.permutations(alphabet)
    for key_tuple in all_keys:
        key = ''.join(key_tuple)
        decrypted_message = decrypt(ciphertext, key)
        print(f"Key: {key}\nDecrypted Message: {decrypted_message}\n")

# Input encrypted message
ciphertext = input("Enter the encrypted message: ")

# Start brute force decryption
brute_force_decrypt(ciphertext)