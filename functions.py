
def multiple_items(*args):
    print(args)
    print(type(args))
    print(args[0])

multiple_items("Ashley", "Michael", "Drew")

my_dictionary = {
    "Ashley":"Hacker",
    "Jaylen": "Coder",
    "George": "GRC Master",
}
multiple_items(my_dictionary)
print(my_dictionary)