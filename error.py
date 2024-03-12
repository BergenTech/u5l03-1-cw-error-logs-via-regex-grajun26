import json, csv, re

with open("logs.json",'r') as jsonfile:
    data = json.load(jsonfile)
    with open("logs.csv",'w',newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = data[0])
        writer.writeheader()
        pattern = r"^Error"
        for x in data:
            if re.search(pattern, x["message"]):
                writer.writerows(data)
            else:
                pass