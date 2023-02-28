country = {4: 3}
print(country[4])

cs = {"code": "UA", "name": "Ukranian", "population": 42}
#cs = dict(code="UA", name="Ukranian")
print(cs["name"])
print(cs)

#print(cs.items())

for key, value in cs.items():
    print(key, " - ", value)


print(cs["name"])
print(cs.get("code"))
#cs.clear()
#cs.pop("name")
#cs.popitem()
#cs.values()

cs["code"] = "UKR"
print(cs.items())

person = {
    "user_1": {
        "first_name": "John",
        "last name": "Marley",
        "age": 45,
        "address": ["c. Izmir", "somewhere", "45"],
        "grades": {"Math": 5, "Physics": "3"}
    },
    "user_2": {

    }
}

print(person["user_1"]["address"][1])



