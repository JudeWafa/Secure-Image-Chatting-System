# Secure-Image-Chatting-System

This project is a preview of a secure chatting system for images. To securely encrypt and decrypt images, Elliptic Curve Cryptography is used.

For each image, an object "Elliptic" is created, with data members "a" and "b" corresponding to coefficents in the elliptic curve function.
Data member "p" as the prime number defining the finite field. "xg" and "yg" being the coordinates of the point G.

Image is then compressed to a size of 146 x 96. And then the image is encrypted using a random point on the curve and the derived public key of the sender.

Entropy analysis and Histogram analysis is then used to measure the security of the encryption process.

Decryption was done by reversing the encryption process.

An indivitual file is made for the "Elliptic" class and the encrypt and decrypt functions. "Main.py" can be used to test encrypting and decrypting on certain images.


