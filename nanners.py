"""suddenly...thousands of them"""

import shutil
from time import sleep

FRUIT = "BANANAS!"
columns = shutil.get_terminal_size().columns

print('This shit is bananas!'.center(columns))
sleep(0.5)

for letter in FRUIT:
    print(letter.center(columns))
    sleep(0.1)

sleep(0.5)
print('\U0001F34C'.center(columns))
# breathe me in, sweet suffering
