level = 25
name = "Link"
character_class = "Wind Runner"
account_active = True
pvp_rank = "Squire"
max_health = 79
max_mana = 274
armor = 12
magic_resistance = 15.4

print("Character Report")
print(f"{name} is a level {level} {character_class}, ranked as a {pvp_rank}.")
print(f"They have {max_health} max health and {max_mana} max mana.")
print(f"They have {armor} armor and {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("Character Report Complete")
print(
    f"Data types {type(level)}, {type(name)}, {type(character_class)}, {type(account_active)}, {type(pvp_rank)}, {type(max_health)}, {type(max_mana)}, {type(armor)}, {type(magic_resistance)}"
)
