#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def user_name(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button run the script.
if __name__ == '__main__':
    user_name('Client')
from PIL import Image
import random
import numpy as np
import tkinter as tk
from tkinter import filedialog


def encrypt_image(input_path, output_path, key):
    try:
        # Load the image
        img = Image.open(input_path)
        img = img.convert("RGB")  # Ensure it's in RGB format
        pixels = np.array(img)

        # Pixels encryption using a simple XOR operation with the key
        encrypted_pixels = np.copy(pixels)
        for i in range(encrypted_pixels.shape[0]):
            for j in range(encrypted_pixels.shape[1]):
                for c in range(3):  # RGB channels
                    encrypted_pixels[i, j, c] ^= key

        # Saving encrypted image
        encrypted_img = Image.fromarray(encrypted_pixels)
        encrypted_img.save(output_path)
        print(f"Image encrypted and saved to {output_path}")

    except Exception as e:
        print(f"Error during encryption: {e}")


def decrypt_image(input_path, output_path, key):
    try:
        # Loading encrypted image
        img = Image.open(input_path)
        img = img.convert("RGB")  # Ensure it's in RGB format
        pixels = np.array(img)

        # Decrypted pixels using the same XOR operation with the key
        decrypted_pixels = np.copy(pixels)
        for i in range(decrypted_pixels.shape[0]):
            for j in range(decrypted_pixels.shape[1]):
                for c in range(3):  # RGB channels
                    decrypted_pixels[i, j, c] ^= key

        # Saving decrypted image
        decrypted_img = Image.fromarray(decrypted_pixels)
        decrypted_img.save(output_path)
        print(f"Image decrypted and saved to {output_path}")

    except Exception as e:
        print(f"Error during decryption: {e}")


def generate_random_key():
    # Generating a random key for XOR encryption (between 0-255)
    return random.randint(0, 255)


def select_image_file(title):
    #Opens file dialog to select an image file
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title=title,
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    return file_path


def save_image_file(title):
    #Opens a file dialog to select a location to save an image.
    root = tk.Tk()
    # Hide the root window
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        title=title,
        defaultextension=".jpg",
        filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png"), ("All files", "*.*")]
    )
    return file_path


if __name__ == "__main__":
    # User selects image for encryption
    print("Select the image to encrypt:")
    input_image_path = select_image_file("Select Image to Encrypt")
    if not input_image_path:
        print("No image selected, exiting.")
        exit(1)

    # Allows user to select the location to save the encrypted image
    encrypted_image_path = save_image_file("Save Encrypted Image")
    if not encrypted_image_path:
        print("No location selected to save encrypted image, exiting.")
        exit(1)

    # Random key generation for encryption
    encryption_key = generate_random_key()
    print(f"Generated encryption key: {encryption_key}")

    # Encrypting the image
    encrypt_image(input_image_path, encrypted_image_path, encryption_key)

    # User select the encrypted image for decryption
    print("Select the encrypted image to decrypt:")
    encrypted_image_path_to_decrypt = select_image_file("Select Encrypted Image to Decrypt")
    if not encrypted_image_path_to_decrypt:
        print("No encrypted image selected, exiting.")
        exit(1)

    # User select the location to save the decrypted image
    decrypted_image_path = save_image_file("Save Decrypted Image")
    if not decrypted_image_path:
        print("No location selected to save decrypted image, exiting.")
        exit(1)

    # Decrypting the image using the same encryption key
    decrypt_image(encrypted_image_path_to_decrypt, decrypted_image_path, encryption_key)


# In[ ]:




