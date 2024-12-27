from bs4 import BeautifulSoup
from urllib import request as req, error as err

wikipedia_main_page: str = "https://en.wikipedia.org/wiki/Prime_knot"

def main():
    try:
        with req.urlopen(wikipedia_main_page) as response:
            soup = BeautifulSoup(response, "html.parser")
    except err.URLError as error:
        print(f"Could not open URL: {error}")
        exit(0)

    # Let's create a dictionary that contains the number of prime knots
    # for a given number of crossings. 
    prime_knots: dict[int: int] = {}

    # We begin by getting a list of all the tables
    table = soup.find("table")
    rows = table.find_all("tr")
    first_row = rows[0]
    second_row = rows[1]
    for index, no_crossings in enumerate(first_row.find_all("td")):
        no_prime_knots = second_row.find_all("td")[index]
        prime_knots[int(no_crossings.text.strip())] = int(no_prime_knots.text.strip())
    # This can be done using zip as well
    # for no_crossings, no_prime_knots in zip(first_row.find_all("td"), second_row.find_all("td")):
        # prime_knots[int(no_crossings.text.strip())] = int(no_prime_knots.text.strip())

    for no_crossings, no_prime_knots in prime_knots.items():
        print(f"There {"are" if no_prime_knots != 1 else "is"} {no_prime_knots} prime knot{'s' if no_prime_knots != 1 else ''} with {no_crossings} crossing{'s' if no_crossings != 1 else ''}.")

if __name__ == "__main__":
    main()
