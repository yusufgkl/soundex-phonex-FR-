import json

with open('./clean_final.json') as f:
    data = json.loads(f.read())

print len(data)
