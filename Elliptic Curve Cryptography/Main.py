import Elliptic 
from EncryptECC import encrypt_to_disk
from DecryptECC import decrypt_to_pic
import imgToDat
import numpy as np
import math
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image

def encryptedImage(filename):
    # Read the text file and parse the coordinates and cipher values
    with open(filename, "r") as file:
        lines = file.readlines()

    # Extract coordinates and cipher values from each line
    coordinates = []
    cipher_values = []
    for line in lines:
        line = line.strip().replace("[", "").replace("]", "").split()
        x = int(line[0][:-1])  # Remove comma from the end of the first element
        y = int(line[1][:-1])  # Remove comma from the end of the second element
        cipher = int(line[2])
        coordinates.append((x, y))
    cipher_values.append(cipher)

    # Determine image dimensions
    max_x = max(coord[0] for coord in coordinates)
    max_y = max(coord[1] for coord in coordinates)

    # Create an empty image array
    image = np.random.randint(0, 256, size=(max_x + 1, max_y + 1), dtype=np.uint8)

    # Display the encrypted image
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()




if __name__ == '__main__':

    ##################### Encryption ####################
    fname = "./input_image.jpeg"
    encrypt, plain = encrypt_to_disk(fname)
    size = Image.open(fname).size
    f = open("encrypt.txt")
    

    encryptedImage("encrypt.txt")


    ################### Entropy Analysis ###################

    cipher = [i[2] for i in encrypt]
    counts = Counter(cipher)
    total_count = len(cipher)
    probabilities = [count / total_count for count in counts.values()]
    entropy = -np.sum(probabilities * np.log2(probabilities))
    
    print(f"Entropy = {entropy}")



    ################## Histogram Analysis ###################

    counts, bins = np.histogram(cipher, bins=500) 
    plt.figure(figsize=(10, 6))
    plt.hist(cipher, bins=500, color='skyblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Cipher Values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Cipher Values')
    plt.grid(True)
    plt.show()


    
    ##################### Decryption ####################

    de = decrypt_to_pic(encrypt)
    # print(de)
    # print(encrypt)
    ff = open("tttt.txt", 'w')
    ff.write(str(de))
    ff.close()
    # print(de)
    imgToDat.restoreImg(de, "trial.png")

    # if len(plain) == len(de):
    #     print("same length")
    #     for j in range(len(plain)):
    #         if plain[j] != int(de[j]):
    #             print(plain[j], end=' ')
    #         if max(encrypt[j]) > 131000:
    #             print(encrypt[j])
    #     print()
    # else:
    #     print("no equal length")