# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt", "r")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(f"Student name is {line}")

f.close()

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("The file you want to read does not exist.")
finally:
    f.close()