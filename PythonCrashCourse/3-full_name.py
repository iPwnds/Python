first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #use a f-string (f) to combine multiple var values with braces {} around the values; f = format
print(full_name)

print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

favorite_language = " python "
print(favorite_language.lstrip()) #this will strip all the whitespaces at the left of the string
print(favorite_language.rstrip()) #this will strip all the whitespaces at the right of the string
print(favorite_language.strip()) #this will strip all the whitespaces of the string