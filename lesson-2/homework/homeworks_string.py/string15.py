string=input("Enter the sentence:")
acronym="".join(word[0].upper() for word in string.split())
print(acronym)