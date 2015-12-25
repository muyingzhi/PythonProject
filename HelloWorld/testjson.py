import json

obj = [[1,2,3],12,123,{'key1':[1,2,3],'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
print(repr(obj))
print(encodedjson)