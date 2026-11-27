def main():
    records = []  # each record is [name, score]

    # 2.a Reading records
    try:
        with open("scores.txt") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                fields = line.split(",")
                try:
                    name = fields[0]
                    score = int(fields[1])
                except (ValueError, IndexError):
                    continue
                records.append([name, score])
    except FileNotFoundError:
        print("File not found.")
        return

    for record in records:
        if record[0] == "Karim":
            print(record[1])

    print(len(records))

    # 2.b Updating the scoreboard
    kept = []
    for record in records:
        if record[0] == "Maya":
            record[1] = 88
        if record[0] != "Nour":
            kept.append(record)

    with open("scores.txt", "w") as file:
        for record in kept:
            file.write(record[0] + "," + str(record[1]) + "\n")

    with open("pass.txt", "w") as file:
        for record in kept:
            if record[1] >= 60:
                file.write(record[0] + "\n")


main()
