import json

obj = [[1,2,3],12,123,{'key1':[1,2,3],'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
personStr = '{"name":"mike","age":1}'
person = json.dumps(personStr)

print(encodedjson)

decodejson = json.loads(encodedjson)
print(decodejson[3]["key1"])