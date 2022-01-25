def main():
    phrase = input("Ievadiet tesktu:")
    word = phrase.split() 
    wordCount = len(word)
    print("Vardu daudzums tekstā: %s" % wordCount) 
main()