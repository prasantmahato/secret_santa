import pandas as pd
import random

def santa(name):
    if name in santa_pair:
        return str(santa_pair[name]).title()
    return "Santosh SIR"

data = pd.read_excel(r'Section_AB.xlsx') 
df = pd.DataFrame(data, columns=['Name'])

# print(df)
names = df['Name'].to_list()
tmp = list(names)

santa_pair = {}
for x in names:
    curr = random.choice(tmp)
    if curr == x:
        curr = random.choice(tmp)
    tmp.remove(curr)
    if curr not in santa_pair.values():
        santa_pair[x] = curr

'''
i = 1
for x in santa_pair:
    print(f"{i}. {x} : {santa_pair[x]}")
    i+=1

print("\n\t\t\tLet's Find Your Secret Santa...")
while True:
    name_ip = input("\nEnter name or exit: ").upper()
    if name_ip == 'EXIT':
        break
    if name_ip in santa_pair:
        print(f"\n'{name_ip}' your Secret Santa is '{santa_pair[name_ip]}'.!!")
'''