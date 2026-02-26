import json


with open('sample-data.json') as f:
    data = json.load(f)


print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':5} {'MTU':5}")
print("-"*50, "-"*20, "-"*5, "-"*5)

for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    
    dn = attributes.get('dn', '')
    descr = attributes.get('descr', '')
    speed = attributes.get('speed', '')
    mtu = attributes.get('mtu', '')
    
    print(f"{dn:50} {descr:20} {speed:5}   {mtu:6}")