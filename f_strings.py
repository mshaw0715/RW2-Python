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