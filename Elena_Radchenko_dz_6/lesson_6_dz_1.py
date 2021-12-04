with open("nginx_logs.txt") as f:
    data = []
    for line in f:
        line_split = line.split()
        data.append((line_split[0],line_split[5].replace('"',''), line_split[6]))
print(data)

