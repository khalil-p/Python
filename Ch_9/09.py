with open("original.txt") as f:
    content_1 = f.read()

with open("duplicate.txt") as f:
    content_2 = f.read()

if(content_1 == content_2):
    print("Files are matching")
else:
    print("Files are not matching")
