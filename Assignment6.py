import string

alphabet = list(string.ascii_lowercase)
alpha_dict = {alphabet[i]: i+1 for i in range(len(alphabet))}

name = input("Enter Name: ").lower()

letter_values = {letter: alpha_dict[letter] for letter in name if letter in alpha_dict}

print("Values of the letters of name", name, "=", letter_values)

name_value = sum(letter_values.values())

print("The Name", name.capitalize(), "has numeric value =", name_value)