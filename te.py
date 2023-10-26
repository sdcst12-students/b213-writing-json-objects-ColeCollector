

line = open("data.csv","r").read().split("\n")


line = "\n".join(line)
print(line)
data = open("data.csv","w")
data.write(line)
data.close()