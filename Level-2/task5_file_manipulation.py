def word_count(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()   # read all content, make lowercase 

        # Remove punctuation 
        import string
        for ch in string.punctuation:
            text = text.replace(ch, " ")

        words = text.split()   # split into words
        word_dict = {}

        # Count occurrences
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

        # Sort alphabetically
        for word in sorted(word_dict):
            print(f"{word} : {word_dict[word]}")

    except FileNotFoundError:
        print(f"Error: The file '{filename.txt}' does not exist.")


filename = input("Enter the filename: ")
word_count(filename)
