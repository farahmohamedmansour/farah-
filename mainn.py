import string


def clean_input(text):
    text = text.upper().replace("J", "I")  
    text = ''.join(filter(str.isalpha, text))  
    return text


def generate_playfair_matrix(keyword):
    
    keyword = ''.join(sorted(set(keyword), key=keyword.index))  
    keyword = clean_input(keyword)

    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    matrix = keyword + ''.join([letter for letter in alphabet if letter not in keyword])

    
    matrix_2d = [list(matrix[i:i+5]) for i in range(0, len(matrix), 5)]
    return matrix_2d


def display_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


def find_position(matrix, letter):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == letter:
                return i, j
    return None


def encrypt(plaintext, matrix):
    
    pairs = []
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext) and plaintext[i] != plaintext[i + 1]:
            pairs.append(plaintext[i:i + 2])
            i += 2
        else:
            pairs.append(plaintext[i] + 'X')  
            i += 1
    
    ciphertext = []
    
    
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        
        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        
        else:
            col1, col2 = col2, col1

        ciphertext.append(matrix[row1][col1] + matrix[row2][col2])

    return ''.join(ciphertext)


def decrypt(ciphertext, matrix):
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = []

    
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        
        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        
        else:
            col1, col2 = col2, col1

        plaintext.append(matrix[row1][col1] + matrix[row2][col2])

    return ''.join(plaintext).replace("X", "")


def main():
    
    keyword = input("Enter the keyword: ")
    message = input("Enter the message (plaintext/ciphertext): ")

    
    cleaned_keyword = clean_input(keyword)
    matrix = generate_playfair_matrix(cleaned_keyword)

    
    print("\nPlayfair Matrix:")
    display_matrix(matrix)

    
    choice = input("\nDo you want to encrypt or decrypt? (Enter 'encrypt' or 'decrypt'): ").strip().lower()
    message = clean_input(message)

    if choice == 'encrypt':
        ciphertext = encrypt(message, matrix)
        print(f"\nEncrypted ciphertext: {ciphertext}")
    elif choice == 'decrypt':
        plaintext = decrypt(message, matrix)
        print(f"\nDecrypted plaintext: {plaintext}")
    else:
        print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")


if name == "__main__":
    main()