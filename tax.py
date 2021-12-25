from typing import TYPE_CHECKING


salary = int(input("What's your salary amount?\n"))
if salary <= 500000 :
    tax = 0.0
elif salary >= 500001 and salary <= 1000000 :
    tax = 0.1
elif salary >= 1000001 and salary <= 2000000 :
    tax = 0.2
else:
    tax = 0.3
taxpayable = salary * tax
print("Total payable tax = Rs." + str(taxpayable))

