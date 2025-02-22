import os
import string
from collections import Counter

# File names
TEXT_FILE = "sample.txt"
REPORT_FILE = "word_count_report.txt"

# Function to create the file if it does not exist
def create_file():
    print(f"{TEXT_FILE} does not exist. Please enter a paragraph to create the file:")
    text = input("Enter text: ")
    with open(TEXT_FILE, "w") as file:
        file.write(text)
    print(f"{TEXT_FILE} has been created successfully!\n")

# Function to read the file content
def read_file():
    with open(TEXT_FILE, "r") as file:
        return file.read()

# Function to clean and count word frequency
def count_word_frequency(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = text.split()
    
    # Count word occurrences
    word_counts = Counter(words)
    
    return word_counts

# Function to display and save the output
def display_and_save_results(word_counts):
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(5)

    # Console Output
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} {'times' if count > 1 else 'time'}")

    # Save results to report file
    with open(REPORT_FILE, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")
    
    print(f"\nResults saved to {REPORT_FILE}")

# Main function
def main():
    # Check if the file exists, if not, create it
    if not os.path.exists(TEXT_FILE):
        create_file()
    
    # Read file content
    text = read_file()

    # Count word frequency
    word_counts = count_word_frequency(text)

    # Display and save results
    display_and_save_results(word_counts)

# Run the program
main()