import random

VACCINES = ["Moderdna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"******Testing VACCINE {vac}")
    if vac == LUCKY:
        print("##################################")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("##################################")
        print()
        break
    print("XXXXXXXX")
    print("Test Failded")
    print("XXXXXXXX")
    print()

VACCINES = ["Moderdna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"******Testing VACCINE {vac}")
    if vac == LUCKY:
        print("##################################")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("##################################")
        print()
        continue
    print("XXXXXXXX")
    print("Test Failded")
    print("XXXXXXXX")
    print()
