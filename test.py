person = dict({
    "name" : "Al Mamun",
    "Dept" : "CSE",
    "University" : "BUBT",
    "ID" : 184,
    "is_ative" : False,
    "is_completed" : True
})
# person.clear()
print(person.keys())
# print(person.values())
# print(person.items())
for key_name in person.keys():
    if key_name == 'name':
        print("person name is ",person[key_name])
    elif key_name == 'University':
        print("Your University is ",person[key_name])
    else:
        print("key not found")

student_dict1 = {'Aadya': 1, 'Arul': 2, }
student_dict2 = {'Harry': 5, 'Olivia': 6}
student_dict3 = {'Nancy': 7, 'Perry': 9}

# join three dictionaries
student_dict = {**student_dict1, **student_dict2, **student_dict3}
# printing the final Merged dictionary
print(student_dict)
# Output {'Aadya': 1, 'Arul': 2, 'Harry': 5, 'Olivia': 6, 'Nancy': 7, 'Perry': 9}