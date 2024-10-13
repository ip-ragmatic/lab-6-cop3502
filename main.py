MENU = """MENU
-------------
1. Encode
2. Decode
3. Quit
"""


# IAN
def encode(pswd):
    """
    Iterates through each element of pswd and increments each by 3. If the
    digit exceeds 9 when incremented, wrap it back to the beginning of
    single digits.
        7 + 3 => 0
        8 + 3 => 1
        9 + 3 => 2
    """
    encoded = ""
    for char in pswd:
        shifted_num = (int(char) + 3) % 10  # n mod 10 where n < 10 is always n
        encoded += str(shifted_num)  # append shifted_num to encoded string
    return encoded

    # # list comprehension one-liner for funsies
    # return "".join([str((int(char) + 3) % 10) for char in pswd])


# Mary, you work on this
def decode(pswd):
    pass


# IAN
def main():
    while True:
        print(MENU)
        opt_choice = input("Please enter an option: ")

        match opt_choice:
            case "1":
                pswd_unenc = input("Please enter your password to encode: ")
                pswd_enc = encode(pswd_unenc)
                print("Your password has been encoded and stored!\n")

            case "2":
                print(f"The encoded password is {pswd_enc}, and the original password is {decode(pswd_enc)}\n")

            case "3":
                break


if __name__ == "__main__":
    main()
