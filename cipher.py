alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(plain_text, shift_amount, cipher_direction):
    end_text = ""
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            position = alphabet.index(char)
            if cipher_direction == "decode":
                shift_amount *= -1
            new_position = (position + shift_amount) % 26
            new_char = alphabet[new_position]
            if is_upper:
                new_char = new_char.upper()
            end_text += new_char
        else:
            end_text += char
    return end_text


while True:
    direction = input("Type 'encode to encrypt, type decode to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Input the shift number\n"))

    result = caeser(text, shift, direction)
    print(f"The {direction} message is {result}")

    another_round = input("Do you want to encode or decode another message?")
    if another_round != "yes":
        print("Goodbye!")
        break
