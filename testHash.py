import json
from hashlib import sha256

def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary

personalInfo = {"test":"helloworld"}
personHash = sha256(dict_to_binary(personalInfo).encode('utf-8')).hexdigest()
print(personHash)