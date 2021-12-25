import random

computer_choice = random.choice(["CT", "MI", "US", "MR"])

acronyms = ["CT", "MI", "US", "MR"]
abbreviations = ["Computed Tomography", "Molecular Imaging", "UltraSound", "Magnetic Resonance"]

print("Computer's choice of acronym is : " + computer_choice)
print("It\'s expansion is : " + abbreviations[acronyms.index(computer_choice)]) 
