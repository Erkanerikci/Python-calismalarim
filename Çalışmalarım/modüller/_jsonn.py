import json

person = '{"name": "Erkan", "language": ["Python", "C#", "Java"]}'

# json_str = json.dumps(person)
# sonuc = json.loads(json_str)
# sonuc = sonuc["name"]
# print(type(sonuc))



# with open("person.json") as f:
#     sonuc = json.load(f) # Burada bir json dosyasındaki verileri çekiyoruz
#     print(sonuc["name"])
#     print(sonuc["language"])
#     print(sonuc)

person_dict = {
    "name": "Erkan",
    "languages": ["Python","C#"]
}

sonuc = json.dumps(person_dict) #Burada ise bir veriyi json dosyasına kaydediyoruz.
print(type(sonuc))

with open("person.json","w") as f:
    json.dump(person_dict,f)


person_dict = json.loads(person)

sonuc = json.dumps(person_dict,indent=4,sort_keys=True) # Daha okunaklı bir şekilde ekrana çıktı veriyor
print(person_dict)
print(sonuc)