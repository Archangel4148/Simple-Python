
def printGrid(width, height, content):
    position = 0
    for row in range(height):
        print("|", end="")
        for i in range(width):
            print(f" {content[position]} ", end="")
            position += 1
        print("\n|\n", end="")
    print("-" * (int(width * 3.5)))


pwidth = input("Enter the width of the grid: ")
while True:
    try:
        pwidth = int(pwidth)
    except ValueError:
        print("Invalid Input...\n")
        pwidth = input("Enter the width of the grid: ")
        continue
    break

pheight = input("Enter the height of the grid: ")
while True:
    try:
        pheight = int(pheight)
    except ValueError:
        print("Invalid Input...\n")
        pheight = input("Enter the height of the grid: ")
        continue
    break

gridContent = ["*" for i in range(pheight * pwidth)]

while True:
    printGrid(pwidth, pheight, gridContent)

    response = input("Would you like to change the grid? ")
    while response.casefold() not in "yesno":
        print("Invalid response...")
        response = input("Would you like to change the grid? ")

    if response in "yes":
        changePos = input("Input the coordinates of the space you would like to change 'x y': ").replace(", ", "")
        while True:
            try:
                if int(changePos.split()[0]) > pwidth or len(changePos.split()) > 2:
                    print("Invalid Coordinate...")
                    changePos = input("Input the coordinates of the space you would like to change 'x y': ").replace(", ", "")
                else:
                    break
            except ValueError:
                print("Invalid Input...")
                changePos = input("Input the coordinates of the space you would like to change 'x y': ").replace(", ", "")
        x = int(changePos.split()[0])
        y = int(changePos.split()[1])
        print(f"X-Coordinate: {x}\nY-Coordinate: {y}")
        shape = input("What character would you like to change it to? ")
        while len(shape) != 1 or shape == " ":
            print("Invalid Character...")
            shape = input("What character would you like to change it to? ")
            print("Replacement Shape:", shape)
        #Find coord location in list

        targetItem = (pwidth * pheight) - (pwidth * (y-1)) - (pwidth - x)

        gridContent[targetItem - 1] = shape

    else:
        break

print("Alright, here's your final grid:\n\n")
printGrid(pwidth, pheight, gridContent)











