from ruamel.yaml import YAML

yaml = YAML()

data = {
    'name': "Alice",
    'age': 28,
    'city': 'Wonderland'
}

data2 = {
    'name': "Nic",
    'age': 32,
    'city': 'Wonderland'
}

with open('YAML/YAML_operations.yaml', 'r') as file:
    loaded_data = yaml.load(file)
    

with open('YAML/YAML_operations.yaml', 'a') as file:
    file.write("# This is a sample YAML file\n")
    file.write("# It contains user information\n")
    yaml.dump(data, file)

with open('YAML/YAML_operations.yaml', 'a') as file:
    file.write("# This is a sample YAML file\n")
    file.write("# It contains user information\n")
    yaml.dump(data2, file)
    

print(loaded_data)

person_name = loaded_data['person']['name']
person_age = loaded_data['person']['age']
person_city = loaded_data['person']['city']

print("\nPerson Details:")
print(f"Name: {person_name}")
print(f"Age: {person_age}")
print(f"City: {person_city}")