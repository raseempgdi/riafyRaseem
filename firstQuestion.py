f =  open("input.txt","r")
text = f.read()
dictionary = dict()
list = list(text.split())
for i in list:
    dictionary[i] = list.count(i)+1
print(dictionary)


