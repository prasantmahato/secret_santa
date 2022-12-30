import pandas as pd
import random

data = pd.read_excel(r'/Users/prasant/Documents/PES/python_programs/secret_santa/SECTION_A.xlsx') 
df = pd.DataFrame(data, columns=['Name'])

# print(df)
names = df['Name'].to_list()
tmp = list(names)

santa_pair = {}
for x in names:
    curr = random.choice(tmp)
    tmp.remove(curr)
    if curr not in santa_pair.values():
        santa_pair[x] = curr

i = 1
for x in santa_pair:
    print(f"{i}. {x} : {santa_pair[x]}")
    i+=1

while True:
    name_ip = input("\nEnter name to search or exit: ").upper()
    if name_ip in santa_pair:
        print("Your Secret Santa is ",santa_pair[name_ip])
    if name_ip == 'EXIT':
        break