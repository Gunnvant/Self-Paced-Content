### Working with numbers
a = 2
print(a)
print(type(a))

b = 2.0
print(b)
print(type(b))

### Working with string
s1 = "This is a string"
s2 = 'This is also a string'
s3 = '''This too is a string'''
print(type(s1))
print(type(s2))
print(type(s3))

### Strings support slicing
print(s1[0])
print(s1[-1])

### Strings also support common string manipulation tasks
print(s1.lower())
print(s1.upper())

print(s1.split(" "))
print(s1.find('i'))

### Incase one wants to list out the methods that can be used with strings we can look at the dir
print(dir(s1))

### To seek help we can 
print(help(s1.count))

### Lists
l1 = [1,2,3,4,[8,9,10],'a']
for i in l1:
    print(i)
print(l1[0])
l2 = [] 
for i in l1:
    l2.append(i)
print(l2)

### Tuples
t1 = (1,2,3,4,5)
print(t1[2])
for i in t1:
    print(i)

t1[2] = 3

### Sets
s1 = set(('1','a','a','b'))
print(s1)
s2 = set(('a','b','c','c'))
print(s1.intersection(s2))

### Dictionaries
d = {'name':'a','age':29,'prev_companies':['abc','def']}
print(d[0])
d['name']
d['prev_companies']
for i in d:
    print(i)
for i in d:
    print(d[i])
d['new_key'] = 'value'

print('value' in d)

print('new_key' in d)

### File descriptors
con = open("pollution_data.csv","r",encoding='utf-8')
data = con.read()
data_lines = con.readlines()
con.close()
print(data)
print(data_lines)

### Use Context Manager
with open("pollution_data.csv","r",encoding="utf-8") as f:
    data = f.read()
    data_lnes = f.readlines()

print(data[0:100])
print(data_lines[0:10])

