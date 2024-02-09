letters = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(text, shift_no):
    mess = ""
    for i in text:
        if i in letters:
            place = letters.index(i)
            if direction == "encode":
                mess += letters[(place + shift_no) % 25]
            elif direction == "decode":
                mess += letters[(place - shift_no) % 25]
        else:
            mess += i
    print(f"{direction}d text is {mess}")
    return


print("Welcome to the Cipher Game!")
end_game = False
while not end_game:
    direction = input("Type encode to encrypt, decode to decrypt:  ").lower()
    while direction != "decode" and direction != "encode":
        print("Error")
        direction = input("Type encode to encrypt, decode to decrypt:  ").lower()
    message = input("Enter message: ").lower()
    while True:
        shift = int(input("Enter shift number\nNB: Number shouldn't be a multiple of 25: "))
        if shift % 25 != 0:
            break
        else:
            print('Shift number should\'nt be cleanly divided by 25.')

    cipher(message, shift)
    ask = input("Go again? y/n: ")
    if ask == "n":
        end_game = True




