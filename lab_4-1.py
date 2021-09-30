# Auhtor: CMOB 9/30/2021

magic_power = int(input("What is your magic power?: "))
shield_charge = int(input("What is your shield charge?: "))

if not ((magic_power >= 90) and (shield_charge >= 75)):
    print("The dragon burns you to a crisp.")
else:
    print("You defeated the dragon! But the princess is in another castle.")
