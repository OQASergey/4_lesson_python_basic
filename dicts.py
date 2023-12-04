# Словари

a = {
    "key1":123,
    "key2":321
}

maria = {
    "name": "Maria",
    "age": "18",
    "hobbies": ["testing", "reading"]
}

karl = {
    "name": "Karl",
    "age": "21",
    "hobbies": ["marketing", "writing", "boardgames"]
}

print(maria["age"])
print(karl["hobbies"])

users = [maria, karl]
print(users)

print(list(maria.items()))
print(list(karl.keys()))
print(list(maria.values()))

print(maria.get("abcd"))
print(maria.get("abcd", "Такого поля нет"))
print(karl.get("age", "Такого поля нет"))

