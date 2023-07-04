
plain = "arminjp"
cipher = "evqmrnt"

from string import ascii_letters

def encrypt(text, key):
    alpha = ascii_letters
    cipher = ""
    for i in text:
        if i not in alpha:
            cipher += i
            continue
        cipher += alpha[(alpha.index(i) + key) % len(alpha)]

    return cipher

def decrypt(text, key):

    # alpha = ascii_letters
    # plain = ""
    # for i in text:
    #     if i not in alpha:
    #         plain += i
    #         continue
    #     plain += chr(ord(i) - key)

    key *= -1
    plain = encrypt(text, key)

    return plain    

def bruteForce(text):

    brute_force_dict = {}
    alpha = ascii_letters

    for key in range(1, len(alpha)):
        tmpPlain = decrypt(text, key)
        brute_force_dict[key] = tmpPlain

    return brute_force_dict

print(encrypt(plain, 4))
print(decrypt(cipher, 4))
print(bruteForce(cipher))