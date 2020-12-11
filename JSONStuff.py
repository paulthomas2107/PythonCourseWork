import json
from json import JSONEncoder

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)  # formats JSON
print(personJSON)

# Write out the JSON file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# Read JSON and convert back to dictionary
personBack = json.loads(personJSON)
print(personBack)

# Read JSON FILE and convert back to dictionary
with open('person.json', 'r') as file:
    person = json.load(file)
print(person)


# Build object and convert to JSON


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        return {
            'name': o.name,
            'age': o.age,
            o.__class__.__name__: True
        }
    else:
        raise TypeError('Object is not JSON Serializable')

# Build and convert


user = User('Paul', 29)
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# Another way


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {
                'name': o.name,
                'age': o.age,
                o.__class__.__name__: True
            }
        return JSONEncoder.default(self, o)


user = User('Paul', 29)
userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)
# or
userJSON = UserEncoder().encode(user)
print(userJSON)
# Back to JSON dictionary
user = json.loads(userJSON)
print(type(user))
print(user)

# or use decoder to convert from JSON


def decode_user(dic):
    if User.__name__ in dic:
        return User(name=dic['name'], age=dic['age'])
    return dic


print("*" * 40)
user = json.loads(userJSON, object_hook=decode_user)
print(user.name)
print(user.age)
