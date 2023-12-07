import sys

ciphertext = str(sys.argv[1])
common_words = ["a", "about", "all", "also", "and", "as", "at", "be", "because", "but", "by", "can", "come", "could", "day", "do", "even", "find", "first", "for", "from", "get", "give", "go", "have", "he", "her", "here", "him", "his", "how", "I", "if", "in", "into", "it", "its", "just", "know", "like", "look", "make", "man", "many", "me", "more", "my", "new", "no", "not", "now", "of", "on", "one", "only", "or", "other", "our", "out", "people", "say", "see", "she", "so", "some", "take", "tell", "than", "that", "the", "their", "them", "then", "there", "these", "they", "thing", "think", "this", "those", "time", "to", "two", "up", "use", "very", "want", "way", "we", "well", "what", "when", "which", "who", "will", "with", "would", "year", "you", "your", "is"]
finalText = ""
max_word_count = -1

for shift in range(26):
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = ord(char) - shift

            if shifted < ord('a'):
                shifted += 26

            decrypted_char = chr(shifted)
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    word_count = 0
    for word in common_words:
        if word in decrypted_text.lower():
            word_count += 1
    if word_count > max_word_count:
        finalText = decrypted_text
        max_word_count = word_count

print("My final guess:", finalText)
