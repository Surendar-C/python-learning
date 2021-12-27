from abc import abstractproperty
import random

computer_choice = random.choice(["CT", "MI", "US", "MR"])

lst = []

print("list --> ", lst)

acronyms = ["CT", "MI", "US", "MR"]
abbreviations = ["Computed Tomography", "Molecular Imaging", "UltraSound", "Magnetic Resonance"]

print("Computer's choice of acronym is : " + computer_choice)
print("It\'s expansion is : " + abbreviations[acronyms.index(computer_choice)]) 

print("length:", len(abbreviations))
abbreviations.append("Diagnostics")
abbreviations.insert(1, "Strategy")
print("length:", len(abbreviations))
print("businesses : ", abbreviations[1:2])
abbreviations.extend(["Marketing", "SHUI", "Syngo"])
print("length:", len(abbreviations))
print("newly modified list", abbreviations)

print("popped element from list : ", abbreviations.pop())
print("length:", len(abbreviations))
print("newly modified list", abbreviations)


