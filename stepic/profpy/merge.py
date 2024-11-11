import json

with open('data1.json') as file1, open('data2.json') as file2:
    data_j1 = json.load(file1)
    data_j2 = json.load(file2)
    data_all = data_j1 | data_j2

with open('data_merge.json', 'w', encoding='utf8') as file_out:
    file_out.write(json.dumps(data_all, indent=3))