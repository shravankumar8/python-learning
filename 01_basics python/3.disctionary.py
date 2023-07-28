# dictionary is nothing but objects these objects store key and valuepairs 

user1={
    "name": "John",
    "age": 18,
    "surname":"lingampally",
    "idno":576576574
}
print (user1["name"])
print (user1["age"])
print (user1["surname"])
print (user1.get("name","nahi"))
# the way to acces a disctionary is using the object.get(keyvalue)
# or we can you use the object["key"]