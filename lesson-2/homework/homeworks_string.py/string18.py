sentence=input("Enter the sentence:")
starts_with=input("Enter the word that starts with:")
ends_with=input("Enter the word that ends with:")

if sentence.startswith(starts_with) and sentence.endswith(ends_with):
    print(f"Yes it starts with {starts_with}, and ends with {ends_with}")
else:
    print("No the sentence does not starts and ends with them")