
try:
    with open("dustrecordings.csv", "r") as dust_readings:
        string_containing_things: str = dust_readings.read()
except FileNotFoundError:
    print("Yeah nah bro")
    exit(0)



lines: list[str] = string_containing_things.split("\n")

data: dict[str: list[float]] = {}

for csl in string_containing_things.split("\n")[1:]:
    if csl != "":
        attributes: list[str] = csl.split(",")
        room: str = attributes[2]
        value: float = float(attributes[1])
        if room not in data.keys():
            data[room] = [value]
        else:
            data[room].append(value)




