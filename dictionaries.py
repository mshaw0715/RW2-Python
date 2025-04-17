# dictionaries
band = {
    "vocals": "Plant", 
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

print(band["vocals"])
print(band.get("guitar"))

print(band.keys())

print(band.values())

print(band.items())

print("guitar" in band)
print("triangle" in band)

band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# band2 = band # create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Ashley"
# print(band)

band2 = band.copy()
band2["drums"] = "Ashley"
print("Good copy!")
print(band)
print(band2)

band3 = dict(band)
print("Good copy!")
print(band3)

member1 = {
    "name": "Plant"
    "instrument" : "vocals"
}
member2 = {
    "name": "Page"
    "instrument": "guitar"
}
band = {
    "member1": member1, 
    "member2": member2
}
print(band)