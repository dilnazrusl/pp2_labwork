import json

# 1. Загружаем данные из файла
with open('sample-data.json') as f:
    data = json.load(f)

# 2. Печатаем заголовок таблицы 
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 50 + " " + "-" * 20 + " " + "-" * 10 + " " + "-" * 10)

# 3. Перебираем интерфейсы и выводим данные
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    
    dn = attributes.get('dn', '')
    descr = attributes.get('descr', '')
    speed = attributes.get('speed', '')
    mtu = attributes.get('mtu', '')
    
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<10}")