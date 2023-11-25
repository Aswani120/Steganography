import cv2

d={}
c={}
for i in range(255):
    d[chr(i)]=i
    c[i] = chr(i)

def encode():
    i_nam = input("\nEnter image name(with extension):")
    img = cv2.imread(i_nam)
    msg = input("Enter secert message:")
    pswd = input("Set password:")
    enc = pswd + '*0' + msg + '##'
    m=0
    n=0
    z=0
    for i in range(len(enc)):
        img[n,m,z] = d[enc[i]]
        n=n+1
        m=m+1
        z=(z+1)%3
    o_nam = input("\nEnter new image name(without extension):")
    cv2.imwrite(o_nam + '.png',img)
    print("\nReturning to Main Menu.")

def decode():
    i_nam = input("\nEnter image name(without extension):")
    img = cv2.imread(i_nam + '.png')
    message =""
    n=0
    m=0
    z=0
    while True:
        if message[-2:] == "##":
            break
        message = message + c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1) % 3
    while True:
        pas = input("Enter password:")
        if pas == message.split('*0')[0]:
            print("\nDecrypted message:",message.split('*0')[1][:-2])
            break
        else:
            print("Wrong Password\n")
    print("\nReturning to Main Menu.")

while True:
    print("\n## Welcome to Stegnography ##\n")
    print("1. Encode\n2. Decode\n3. Quit\n")
    while True:
        opt = input("Choose an option:")
        if opt == '1':
            encode()
            break
        elif opt == '2':
            decode()
            break
        elif opt == '3':
            quit()
