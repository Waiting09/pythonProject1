import json

data = [{'a': 1, 'b': '2', 'c': True, 'd': False, 'e': None}]
# dumps()：将 Python 对象编码成为JSON 字符串
print(json.dumps(data))
# loads()：将 JSON 字符串解码为 Python 对象
json_data = '''[{"a": 1, "b": "2", "c": true, "d": false, "e": null}]'''
print(json.loads(json_data))
# dump()： 将Python 对象转换成 JSON格式，并将数据写入 json 文件中
# with open('json_data', 'w+', encoding='utf-8') as j:
#     json.dump(data,j)
# # load()：从 json 文件中读取数据并解码为 Python 对象
with open('json_data', 'r', encoding='utf-8') as f:
    print(json.load(f))


#中文
data1 = {'a': 1, 'b': '霍格沃兹', 'c': True, 'd': False, 'e': None}
print(json.dumps(data1, ensure_ascii=False, indent=4))
