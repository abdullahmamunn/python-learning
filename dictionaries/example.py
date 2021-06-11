#declare a initial dictonaries
person = {
    "name": "Abdullah",
    "skill": "Python",
    "phone": 0o54351213214,
    "is_valid": True,
    "birth_date": "5 june 1995"
}
# person["birth_date"] = "June 5 1997"
print(person.get("name"))
print('key' ' : ' 'value')
for info in person.items():
    # print(info, ':', person[info]) #without items()
    print(info[0], ":", info[1]) #using items()

number = input("numbers: ")
output = ""
number_mapping = {
    "1": "one",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
for ch in number:
    output += number_mapping.get(ch, "!") + " "
print(output)