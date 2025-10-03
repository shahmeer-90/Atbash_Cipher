
def atbash_cipher(text):
    result = ""

    for char in text:
        if char.isalpha(): 
            if char.isupper():
                
                result += chr(65 + (90 - ord(char)))
            else:
                
                result += chr(97 + (122 - ord(char)))
        else:
            
            result += char

    return result



if __name__ == "__main__":
    plaintext = input("Enter your message: ")
    
    
    encrypted = atbash_cipher(plaintext)
    print("Encrypted Text:", encrypted)
    
    
    decrypted = atbash_cipher(encrypted)
    print("Decrypted Text:", decrypted)
