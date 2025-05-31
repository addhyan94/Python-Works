import time

print("Welcome to ~~~~")
print("Jadoo Ka Dimaag Padhne Wala!")
print("Socho koi bhi 2 digit number (10 se 99 ke beech)...")
time.sleep(2)
print("Us number ke dono digits ka sum nikalo...")
time.sleep(2)
print("Ab asli number me se digit sum minus karo...")
time.sleep(2)
print("Ab result ke saamne diye hue symbols me dekho...")
time.sleep(2)

symbols = ['@', '#', '$', '%', '&', '!', '*', '?', '~']
import random
magic_symbol = random.choice(symbols)

# Create symbol chart
for i in range(100):
    if i % 9 == 0:
        print(f"{i} - {magic_symbol}")
    else:
        print(f"{i} - {random.choice(symbols)}")

input("\nSocha? Ab Enter dabao aur dekho Jadoo!")
print("\nTumhara symbol hai:", magic_symbol)
