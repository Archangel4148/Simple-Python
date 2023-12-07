response = input("Would you like to encode or decode? ").casefold()
key = input("What will your key be? ")
visible = input("Would you like to show additional info? (y/n): ").casefold()
while True:
    try:
        key = int(key)
        break
    except ValueError:
        print("Invalid key number...")
        key = input("What will your key be? ")
        continue

while response != 'encode' and response != 'decode':
    print("Invalid input...\n")
    response = input("Would you like to encode or decode? ")

while visible not in "yes" and visible not in "no":
    print("Invalid input...\n")
    visible = input("Would you like to show additional info? (y/n): ").casefold()

if visible in 'yes':
    visible = True
else:
    visible = False

if response == 'encode':
    plaintext, binList = input("Enter the message: "), []
    for i in plaintext:
        if visible:
            print("_______________\nCharacter:", i, "\nDecimal:", ord(i))
        bString = bin(ord(i)).replace("0b", "")
        if visible:
            print("Binary:", bString)
        for i in range(key):    
            bString = bString[1:] + bString[0]
        if visible:
            print("Shifted:", bString)
        binList.append(bString)
    eString = ' '.join(binList)
    codeString = ""
    print(f"\nEncoded String: {eString}")
    for i in eString.split():
        codeString += str(chr(int(i, 2)))
    if visible:
        print(f"Fake Code String: {codeString}")
    
else:
    codeText, plaintext, decode = input("Enter the encoded string: "), "", True
    for i in codeText:
        if i not in "01 ":
            print("Sorry, this string isn't in binary...")
            decode = False
            break
    if decode:
        for chunk in codeText.split():
            if visible:
                print("_______________\nBinary:", chunk)
            for i in range(key):
                chunk = chunk[-1] + chunk[:-1]
            if visible:
                print("Corrected Binary:", chunk)
                print("Decimal:", int(chunk, 2))
                print("Character:", chr(int(chunk, 2)))
            plaintext += chr(int(chunk, 2))
        print("\nDecoded String:", plaintext)

exit = input("Press Enter to Close...")
                

