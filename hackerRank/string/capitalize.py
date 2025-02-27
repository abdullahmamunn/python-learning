x = input()
full_name = x[:].split()
for name in full_name:
    x = x.replace(name,name.capitalize())
print(x)
# explanation
# split() function done the separation between string
# loop through in the full_name and first index is first name
# and we replace the first name and capitalize it, and so on...
