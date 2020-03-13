letter = input("Enter letter: ")
consonants = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
vowels = ("a","e","i","o","u")
if letter.lower() in consonants:
  print(letter, " is a consonants")
elif letter.lower() in vowels:
  print(letter, "is a vowel")