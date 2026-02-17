print("Hello! Welcome to the Band Name Generator")
city = input("What's the name of the city you grew up in ?\n ")
pet = input("What is the name of the pet ?\n ")
mix = city[:3] + pet[-3:]

print("Your band name could be: " + mix)
