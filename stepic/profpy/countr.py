import json

# Читаем данные из файла countries.json
with open('countries.json', encoding='utf-8') as file:
    countries_data = json.load(file)

# Создаем словарь для хранения религий и соответствующих стран
religion_dict = {}

# Обрабатываем данные
for entry in countries_data:
    religion = entry['religion']
    country = entry['country']
    
    # Если религия еще не добавлена в словарь, создаем новый список
    if religion not in religion_dict:
        religion_dict[religion] = []
    
    # Добавляем страну в список для данной религии
    religion_dict[religion].append(country)

# Записываем результат в файл religion.json
with open('religion.json', 'w', encoding='utf-8') as outfile:
    json.dump(religion_dict, outfile, ensure_ascii=False, indent=4)

print("Данные успешно записаны в файл religion.json")