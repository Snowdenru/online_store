import sqlite3

conn = sqlite3.connect('Github/online_store/products.db')

cursor = conn.cursor()

data = []
with open('Github/online_store/category.txt', 'r') as f:
    for i in f:
        data1 = i.split(', ')
        data.append(tuple([int(data1[0]), data1[1]]))

cursor.executemany('Insert or ignore into Category Values (?, ?)', data)
conn.commit()

data = []
with open('Github/online_store/status.txt', 'r') as f:
    for i in f:
        data2 = i.split(', ')
        data.append(tuple([int(data2[0]), data2[1]]))

cursor.executemany('Insert or ignore into Status Values (?, ?)', data)
conn.commit()

data = []
with open('Github/online_store/Products.txt', 'r') as f:
    for i in f:
        data3 = i.split(', ')
        data.append(tuple([int(data3[0]), data3[1], int(data3[2]), int(data3[3]), int(data3[4]), int(data3[5])]))

cursor.executemany('Insert or ignore into Products Values (?, ?, ?, ?, ?, ?)', data)
conn.commit()


conn.close()

