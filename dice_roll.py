import random


def next_no():
    no = random.randrange(1, 7)
    input_again = input("Ready for roll??   Enter=roll   Q=Quit")
    if input_again.lower() != 'q':
        print(no)
        next_no()
    else:
        print("Thank you for playing")


next_no()
