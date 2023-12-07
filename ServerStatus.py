from mcstatus import JavaServer

ip = input("Enter server IP: (Press Enter to default to Multirotor server): ")

# You can pass the same address you'd enter into the address field in minecraft into the 'lookup' function
# If you know the host and port, you may skip this and use JavaServer("example.org", 1234)
if ip == "":
    ip = "multirotor.lit.ai"

server = JavaServer.lookup(ip)
# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
# Don't expect the player list to always be complete, because many servers run
# plugins that hide this information or limit the number of players returned or even
# alter this list to contain fake players for purposes of having a custom message here.
status = server.status()
print(f"\nServer IP: {ip}\nPlayers Online: {status.players.online}\n")

# 'query' has to be enabled in a server's server.properties file!
# It may give more information than a ping, such as a full player list or mod information.
if status.players.online > 0:
    query = server.query()
    print("Players Online:")
    print('\n'.join(query.players.names))

input("\nPress Enter to quit...")