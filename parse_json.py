"""" JavaScript Object Notation """

import json
conversions = '''

        JSON                    Python
        
        object                  dict
        array                   list
        string                  str
        number(int)             int
        number(real)            float
        true                    True
        false                   False
        null                    None

'''

people_string = '''
{
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL"
    },
    {
      "name": "Alaska",
      "abbreviation": "AK"
    },
    {
      "name": "Wyoming",
      "abbreviation": null
    }
]
}

'''

# Here we loaded string to  python objects and loaded back the json
data = json.loads(people_string)
print(type(data['states']))

for i in data['states'] :
    del i['abbreviation']

new_string = json.dumps(data,indent=1,sort_keys=True)
print(new_string)

# Operation with the files
import json
with open('sample data/states.json') as f:
    data = json.load(f) # loading the json file into python object

# NOTE : json.load() used to load a file
#        json.loads() used to load a string
#        dump() used to dump a file
#        dump() used to dump a string

for state in data['states']:
    del state['area_codes']

with open('new_json.json','w') as f:
    json.dump(data,f,indent=2)

# Accessing the json data from the public API
import json
from urllib.request import urlopen
with urlopen("https://gmail.googleapis.com/$discovery/rest?version=v1") as response:
    source = response.read()


# print(source) # this is a response given by the API now we need to convert it into the python object

data = json.loads(source) # python object

#print(json.dumps(data,indent=2))

#print(len(data['states']['name']))
for item in data['states']['name'] :
    print(item)
