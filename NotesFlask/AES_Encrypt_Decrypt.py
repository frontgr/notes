from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def aes_encryption(data):

    # data_to_encrypt = data['content'].encode()
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce

    ciphertext = cipher.encrypt(data)

    # data['content'] = ciphertext
    return ciphertext, key, nonce


def aes_decryption(note_to_decrypt, key, nonce):

    cipher2 = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher2.decrypt(note_to_decrypt).decode('utf-8')
