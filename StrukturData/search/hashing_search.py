hash_table = [None] * 10
def hashfunction(value):
    return value % len(hash_table)

def insert(hash_table, value):
     hash_key = hashfunction(value)
     hash_table[hash_key] = value
     
def search(value):
    return hashfunction(value)

insert(hash_table, 5)
insert(hash_table, 12)
insert(hash_table, 36)
insert(hash_table, 7)
insert(hash_table, 27)
print(hash_table)
print(search(7))