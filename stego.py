import cv2
import os

def encrypt_message(image_path, secret_message, password):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Unable to load image.")
        return

    char_to_int = {chr(i): i for i in range(255)}
    int_to_char = {i: chr(i) for i in range(255)}

    n, m, z = 0, 0, 0
    for char in secret_message:
        img[n, m, z] = char_to_int[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite("EncryptedMsg.jpg", img)
    print("Encryption complete")

    os.system("start EncryptedMsg.jpg")

    passcode = input("Enter passcode for Decryption: ")

    if password == passcode:
        decrypted_message = ""
        n, m, z = 0, 0, 0
        for i in range(len(secret_message)):
            decrypted_message += int_to_char[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3

        print("Decryption message:", decrypted_message)
    else:
        print("Invalid passcode")