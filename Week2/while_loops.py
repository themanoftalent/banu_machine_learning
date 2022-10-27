print("####### 1 sayinin toplami ##########")


def sayiHesaple():
    current_number = 2
    while current_number <= 200:
        twice_number = current_number + current_number
        print(f"{current_number} and {current_number} are {twice_number}")
        current_number = twice_number
    print("####### 1 eklenince ##########")

    current_number = 2
    while current_number <= 200:
        twice_number = current_number + current_number
        print(f"{current_number} and {current_number} are {twice_number}")
        current_number = twice_number + 1
    print("######## 3 eklenince #########")

    current_number = 2
    while current_number <= 200:
        twice_number = current_number + current_number
        print(f"{current_number} and {current_number} are {twice_number}")
        current_number = twice_number + 3
    print("######## carpimi #########")

    currentsayi = 2
    while currentsayi < 4294967296200018446744073709551616:
        twicesayi = currentsayi * currentsayi
        print(f"{currentsayi} and {currentsayi} are {twicesayi}")
        currentsayi = twicesayi


sayiHesaple()
