a = open("kitxvebi.txt", "r", encoding="utf-8")
for each in a.readlines():
    print(each, end="")
a.close()  # Always close the file when you're done with it