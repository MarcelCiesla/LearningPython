print("This IT Organization has various skill sets")
print("Find out your match...")

print("Enter Capitalised Values:")

DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Docker", "Kubernetes", "Terraform"]
Development = ("NodeJs", "AngularJs", "Java", ".net", "Python")
cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
cntr_emp2 = {"Name":"Santa", "Skill":"AI", "Code":1218}

usr_skill = input("Enter your desired skill: ")
print(usr_skill)

# Check in the database if we have this skill
if usr_skill in DevOps:
    print(f"We have {usr_skill} in DevOps Team.")
elif (usr_skill in Development):
    print(f"we have {usr_skill} in Development Team")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"we have contract employees with this {usr_skill}")
else:
    print("Skill not found")
