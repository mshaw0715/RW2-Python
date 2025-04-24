
name = "Ashley" #this is a global scope
count = 1

# def greeting():
#     color = "Black"
#     print(name)
#     return color # this is a local scope


# color = greeting()
# print(color)

# def another():
#     greeting("Michael")

# another()

def another():
    color = "Black"
    # count += 1
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "Blue"
        print(color)
        print(name)

    greeting("Ashley")

another()