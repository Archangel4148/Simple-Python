#Establish starting variables (applesauce total)
while True:
    try:
        sauce = int(input("How many applesauces do you have total? "))
    except ValueError:
        print("Invalid input...\nPlease enter a whole number of applesauces...\n")
        continue
    if sauce == 0:
        print("Well that's just sad. You haven't got any applesauce...\n")
        continue
    if sauce < 0:
        print("How are you supposed to stack negative applesauce? Try again.\n")
        continue
    break

#Making sure inputs are clean so they are usable

stackType = input("Are you stacking on corners, or are the applesauces centered on top of each other?(corners/center): ")

while stackType.casefold() != "corners" and stackType.casefold() != "center":
    print("Invalid Input. Please enter \'corners\' or \'center\'...\n")
    stackType = input("Are you stacking on corners, or are the applesauces centered on top of each other?(corners/center): ")

#Begin calculations for pyramid size

total, sTotal, layer = 0, 0, 0

if stackType == "corners":
    while total < sauce:
        layer += 1
        if sTotal <= sauce:
            total = sTotal
        else:
            layer -= 1
            break
        sTotal += layer ** 2

    layer -= 1   
    print(f" Alright, so with {sauce} applesauces and stacking on corners, you could make a {layer} by {layer} pyramid that is {layer} layers tall, and have {sauce - total} applesauces left over.\n\n")
    
elif stackType == "center":
    while total < sauce:
        layer += 1
        if sTotal <= sauce:
            total = sTotal
        else:
            layer -= 1
            break
        sTotal += (layer*2)**2
    layer -= 1
    print(f" Alright, so with {sauce} applesauces and stacking on centers, you could make a {layer * 2} by {layer * 2} pyramid that is {layer} layers tall, and have {sauce - total} applesauces left over.\n\n")

exit = input("Press Enter to close...\n\n\n")
