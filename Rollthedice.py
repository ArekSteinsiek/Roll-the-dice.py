import random
total = 0
mode = input("Wähle den Modus: easy/normal/hard: ").lower()
if mode == "easy":
    target = 25
elif mode == "normal":
    target = 35
elif mode == "hard":
    target = 50
else:
    print("Ungültiger Modus")
    exit()

choice = input("Roll the dice? (y/n): ").lower()
if choice == "y":
    for x in range(5):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
        total += die1 + die2
    print(f"Gesamtpunktzahl: {total}")
    if total >= target:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
elif choice == "n":
    print("Thank's for playing!")
else:
    print("Invalid choice")
