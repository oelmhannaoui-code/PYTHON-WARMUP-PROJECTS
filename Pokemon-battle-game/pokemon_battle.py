# POKEMON Style Battle

pikachu = {
    "hp": 100,
    "attack": 20
}

charizard = {
    "hp": 120,
    "attack": 18
}

while pikachu["hp"] > 0 and charizard["hp"] > 0:
    charizard["hp"] -= pikachu["attack"]
    print("\nPikachu attacked!")
    print(f"Charizard loses {pikachu['attack']} HP!")
    print(f"Charizard HP: {charizard['hp']}")
    if charizard["hp"] <= 0:
       break
      
    pikachu["hp"] -= charizard["attack"]

    print("----------------------")

    print("\nCharizard attacked!")
    print(f"Pikachu loses {charizard['attack']} HP!")
    print(f"Pikachu HP: {pikachu['hp']}")

if charizard["hp"] <= 0:
    print("Pikachu WON!")
else:
    print("Charizard WON!")
