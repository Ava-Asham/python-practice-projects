name = input("Enter your name: ")

print("Your name: ", name)
print("Number of letters: ", len(name))
print("First letter: ", name[0])
print("Last letter: ", name[-1])
print("Lowercaser version: ", name.lower())
print("The place of the first letter 'a': ", name.find("a"))
print("Data type: ", type(name))