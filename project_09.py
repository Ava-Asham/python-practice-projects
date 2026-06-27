word = input("Enter your word: ")

print("Number of letters: ", len(word))
print("first letter: ", word[0])
print("last letter: ", word[-1])
print("Lowercase version: ", word.lower())
print("The place of the first letter 'a': ", word.find("a"))