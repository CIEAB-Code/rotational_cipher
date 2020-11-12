message = input("Enter secret message: ")
message_valid = False

while not message_valid:
    if len(message) < 1:
        message = input("Enter message: ")
    else:
        message_valid = True

shift = input("Enter amount of letters to shift text (1-25): ")
shift_valid = False

while not shift_valid:
    if shift.isdigit():
        shift = int(shift)
        if shift > 0 and shift < 26:
            shift_valid = True
        else:
            shift = input("Please enter a valid number between 1 and 25: ")

    else:
        shift = input("Please enter a valid number between 1 and 25: ")

coded_message = ''
for char in message:
    if not char.isalpha():
        new_char = char
    elif char.isupper():
        new_ord = (ord(char)) + shift
        if new_ord > 90:
            new_ord -= 26
        new_char = chr(new_ord)
    elif char.islower():
        new_ord = (ord(char)) + shift
        if new_ord > 122:
            new_ord -= 26
        new_char = chr(new_ord)

    coded_message += new_char

print(coded_message)
