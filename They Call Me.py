import random
from os import system
from subprocess import run
system("color A")
output = run("ipconfig", capture_output=True).stdout
ip = str(output[363:374]).replace("b", "").replace("\'", "")

print(f"Your ip is {ip}!")

response = input("Would you like to reset your reference files? (y/n): ")
while response != 'y' and response != 'n':
    print("Invalid input...")
    response = input("Would you like to reset your reference file? (y/n): ")

if response == 'y':
    f = open("names.txt", "w")
    s = open("items.txt", "w")

    s.write("cattle prod\ndeer heart\ncarbeurator\nivory handled spoon\nsmall doll\ndvd box set of the crown\nmalware\nMicheal Jackson's glove\nbox of live bees\nSumerian dagger\nMorbius DVD\nweb shooter that shoots 45acp\nbottle of eye drops\nalchohol marker that doesn't get you drunk\npeter griffin funko pop\nrice cooker\nsamsung galaxy fold\nnokia brick phone\ninfantile gorilla\nfeatherless chicken I call man\ngold ps5\npoorly made cosplay sword\ngoblin tome")
    f.write("Schlatt\nLogan from Big Time Rush\nThe PVP God\ncigarette\nSchlatticus\nSchlatticus Maximus\nJaylor Schwift\nAmazon Prime\nJamaica Schlattville\nJonathan Schlatt\nJay Scott\nJ Money\nJschlitt\nSchlitt\nShroud\nGenocide Schlatt\nNutSchlack\nSchlurp\nJschlatt Basculus\nMr Tekkit\nWork Guy\nChrome Guy\nFlying Man\nFlight Man\nPence Man\nJack Frost\nThe Winner\nNice Catch\nSun Rise Guy\nMr. Fortnite\nMonitor Man\nMr. Goop\nApple man\nDropper Dude\nButton Man\nLadder Man\nBlades\nBuild Boy\nBuild Man\nBuild Bob\nSlur Man\nMr Windex\nStal\nWater Man\nMr SMP Live\nKing of Tekkit\nTekkit\nJschlong\nThe Cuck Shed Man\nJslat\nHomewrecker\nJshmuck\nFlap-Schlatt The Lawnmower\nGay\nGayshat\nThe Parkour God\nFunny Mic\nThe Parkour Prince\nMr Cobble\nMr Cobblestone\nEagle Eyes\nBladez\nShart\nThe Bread Man\nOne half of the Hexxit Hebrews\nHackerman\nFifty Mick\nMr Minecraft\nMr Business\nGreek Philosopher\nGlass Guy\nNice Catch 2\nTwisty Neck\nSlut\nGay Slut\nIsawitcoming\nSack Schlatt\nSweaty Balls\nWilbur's Pretty Princess\nWilbur Schlatt From Schlatt House\nBukowski\nIslam\nNice Shot\nAdolf Schlattler\nHomosexual M Jason Schlatum\nMr Skid\nSchlatt Does Minecraft\nNacho Libre\nSchlittleStick\nFatSchlatt\nJizzSlurp\nPokiman\nJFK\nJacob Schlatt\nIgorsh\nNostalgia Critic\nCosby\nJustin Trudeau\nJMcChill\nSchlatt Bama\nChuck\nProJschlatt\nJoseph Stalin\nSea Cock\nSchlattorious\nShlunk\nJamie Hyneman\nJefferey Epstein\nWilbur\nCarson\nJoko\nFitz\nThe Mist Schlatt\nAntVenom\nTechnoblade\nAlinity\nConnorEatsPants\nConarEatPant\nJoebunga\nPrecum\nAsianschlatt\nCumschlatt\nJoe Jonas\nJohnny Sins\nDad\nJay Hatt\nVideo GameSchlatty\nPewdiepie\nRoll Man\nSea Salt\nSemen. The Amazing Grapist\nA Homo Sexual\nJUULSchlatt\n2 Scoops\nSmokestack\n70 Nic (previously known as 50 Nic)\nJondar\nWall Man\nMail Man\nThe Man with a Plan\nYes Papa\nA Furry\nJebediah\nJebediah Schlatt\nWord Smith\nPoppycock\nTexas Instruments\nBeethoven\nMetronome\nColonel Sanders\nLogan paul\nJFLAT\nJSOUP\nMuscles-Glasses\nNo Plan Andy\nNice Catch\nJackie Robinson's Golden Boy\nWordsmith\nScat\nBaby\nCat-Flap\nVOICEOVERPETE\nSwaggerSouls\nJames Charles\nSchlonic the Hedgehog\nPiledriver\nUh Oh\nNoob Pooper\nTerraria Man\nBig Guy\nNew Guy\nCounter Strike Man\nLW-Sheol\nCockSchlatt\nCringeSchlatt\nMr. Moustache Man\nMr. Rabbit\nThe Age of Empires\nIs Half\nMan\nHot Gay Man\nSinus Infection\nOne Tablet Twice a Day\nHospital\nLittle Girl\nYour Man\nPOOPOO MAN\nDan Schneider\nSchlattina\nThe Sword Man\nJonathan Schlatt\nTiny Dick Man\nTiny Dick Boy\nNinety Thousand Dollars In Debt\nThe Horned Cuck\nSheepBitch\nWilbur Soot\nTraves\nGod\nMr. Health and Safety\nJeff Bezos\nEl Presidente\nMan of Steel\nThe Inventor of Loud = Funny\nSecretary of Steel\nFreddy\nBilingual\nJimmy Neutron\nMagic Fingers\nTwo in a Row\nTwo Piece\nFloyd Mayweather\nAddict\nDyin' Bryan\nMr. 8 Ball\nDouble Time\nDoctor Shakey Jones\nShakey Bones\nShakey\nIsaac Newton\nthe Pool Boy\nHouse Man\nLW-Lanceron\nTyler (Ninja) Blevins\nThe Blev\nThe Man Behind The Slaughter\nSword Man\nThe Fruit Ninja\nMaster Oogway\nGayass\nTony Hawk\nThe Hole In One Man\nLarry the Lobster\nPablo Picasso\nPower Plant\nPower Point\nMr. Minecraft\nMr.Serotonin\nMr. Twitch\nMorton from Mario Kart 8\nThe Blade Runner\nLightning McQueen\nGongaga\nMisfits\nThe Ebay Man\nAn E-boy\nHook Line and Sinker\nThe Fisherman\nThe Hook Man\nThe Pacifier (starring Vin Diesel)\nRenaissance Man\nInspector Gadget\nKatniss Everdeen\nBalls of Fury\nThe Night Owl\nThe North Tower\nWord Hunt\nLuigi\nBeyblade\nMr. Mutton Chops\nCaptain Price\nThe Deity\nThe Curator\nThe Steel Toe\nThe Foot Man\nThe Human Hula Hoop\nWarrior\nFod\nGundham Tanaka\nThe God of Yoga\nThe God of Wii Fit\nScott Slanders\nBovine Boy\nSheldon Cooper\nMaracana\nThe Maraca Man\nPrime Minister of the Gaylord OPPS\nUSPS\nElon Musk\nElton John\nSuccessful Business Man\nWorld Record Rabbids: Go Home Holder\nWater Bitch\nSpacex\nWage Cuck\nMr. Hands\nPaul Walker\nMr. Jellicle\nThe Bread Boy\nSpitshine\nGlizzy Gobbler\nSchlatty Boy\nSwiss Army knife\nMr.knife\nDEFINITELY NOT GAY\nRbxljnP7z3\nSchlagg\nSue Sylvester\nWill Schuester\nJschwatt (widepeepoHappy cumfart streamer)\nThe Roller Coaster Man\nMan of the Scripture\nAschlatt\nBschlatt\nCschlatt\nDschlatt\nEschlatt\nFschlatt\nGschlatt\nHschlatt\nIschlatt\nKschlatt\nLschlatt\nMschlatt\nNschlatt\nOschlatt\nPschlatt\nQschlatt\nRschlatt\nSschlatt\nTschlatt\nUschlatt\nVschlatt\nWschlatt\nXschlatt\nYschlatt\nZschlatt\nJslur\nMutton Man\nWings\nand perhaps the most iconic of all\n'J for Joe Rogan' Schlatt")
    f.close()
    s.close()
else:
    f = open("names.txt", "r")
    s = open("items.txt", "r")
    itemFileText = s.read()
    nameFileText = f.read()
    f.close()
    s.close()

names, items = [], []
f = open("names.txt", "r")
s = open("items.txt", "r")

for i in f.readlines():
    names.append(i.replace("\n", ""))
for i in s.readlines():
    items.append(i.replace("\n", ""))
f.close()
s.close()
print("\n____________________________________________________________\nPress Enter to continue, or type \'quit\' to leave any time!\n____________________________________________________________")
while response != "quit":

    thing = random.choice(items)

    print(f"\n\nThey call me {random.choice(names)}, because of what I did in \'{str(random.randint(1972, 2009))[-2:]} with", end="")
    firstThing = thing.split()[0]

    if firstThing[0] in 'aeiou':
        mid = " an "
    else:
        mid = " a "

    print(mid, end="")

    print(thing)
    response = input()
