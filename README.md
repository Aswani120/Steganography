# Welcome to Steganography
Image Steganography is the process of hiding a secret message in the image such that someone cannot know the presence of the message. There are many methods or algorithms to hide a secret message in the image. This project uses LSB substitution. The LSB substitution makes changes in the least significant bits of pixel to store the message.
## Usage
This project is a command-line interface-based program written in Python. The program can be used to encode or decode the message in the image. The image has to be located in the folder to embed a message in it. The image generated after embedding the message is saved in the same file.
### Encoding
The program has encode option to encode the message in the image. The user has to provide an image file name and the secret message that has to be encoded. Then a password is set which is used to get the decoded message. Then the encoding is done and a new image is saved as a PNG file.
### Decoding
The program has a decode option to decode the message in the image. The user has to provide a message-encoded PNG file to decode the message in it. The user has to provide the password which is set during the encoding. Then we can see the decoded message.
