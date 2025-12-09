with open("example.txt", "w") as file:
    file.write("Hello, Python!")

with open("example.txt", "r") as file:
    print(file.read())  # Hello, Python!
