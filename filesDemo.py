with open('demo.txt', 'r') as reader:
    l = reader.readlines()
    print(l[::-1])

with open('demo.txt', 'w') as writer:
    for w in l[::-1]:
        writer.write(w)


