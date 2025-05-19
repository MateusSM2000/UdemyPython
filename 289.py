import json

string_js = '''
{"a":1, "b":2.2, "c":null, "d":true, "e":false}
'''

conveter_para_python = json.loads(string_js)

print(conveter_para_python)
print(conveter_para_python['a'])


conveter_para_js = json.dumps(conveter_para_python, ensure_ascii=False, indent=2)
print(conveter_para_js)