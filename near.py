


def near (string_main, string_sub):
    list_parent = list(string_main)
    for letter in string_main:
     word_with_letter_removed = string_main.replace(letter, "")
    if word_with_letter_removed == string_sub:
      return True
    return False

word1= input("Enter first word:")
word2= input("Enter first word:")

print(near(word1, word2))