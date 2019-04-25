

import json

with open("countries.json", 'r') as f:
    temp = json.loads(f.read())
    print(str(temp))