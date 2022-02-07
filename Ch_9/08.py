
with open("original.txt") as f:
    content = f.read()

with open("duplicate.txt", "w") as f:
    f.write(content)
