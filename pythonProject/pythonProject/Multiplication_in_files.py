#stores multiplications from 2 to 20 in tables folder in seperate folder for every numbers multiplication
for i in range(2,21):
    table=""
    for j in range(1,11):
        table+=f"{i*j}\n"
    with open(f"tables/table_{i}","w") as f:
        f.write(str(table))