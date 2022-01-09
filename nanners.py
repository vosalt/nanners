"""suddenly...thousands of them"""

import shutil
from time import sleep


def main():
    """hollaback"""
    fruit = "BANANAS!"
    columns = shutil.get_terminal_size().columns

    print("This shit is bananas!".center(columns))
    sleep(0.5)

    for letter in fruit:
        print(letter.center(columns))
        sleep(0.1)

    sleep(0.5)
    print("\U0001F34C".center(columns))


if __name__ == "__main__":
    main()

# breathe me in, sweet suffering
