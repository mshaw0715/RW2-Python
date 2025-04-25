# concatonate to print strings
person = "Ashley"
coins = 3
print("\n" + person + " has " + str(coins) + " coins left.")

# use %s to print strings
message = "\n%s has %s coins left." % (person, coins)
print(message)

# use .format method to print strings
message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

# use f strings to print strings
message = f"\n{person} has {coins} coins left."
print(message)


student = "Ashley"
subject = "Python"

print(f"{student} is studying {subject}\n")

message = f"\n{person} has {2 * 5} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)

num = 10
print(f"\n2.25 times {num} is {2.25 *num:.2f}\n")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25 *num:.2f}")