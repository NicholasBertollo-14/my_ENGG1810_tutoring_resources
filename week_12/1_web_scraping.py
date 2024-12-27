from urllib import request as req, error as err

urls_to_request: dict[str: str] = {
    "example": "https://www.example.com",
    "google": "https://www.google.com/",
    "engg1810": "https://www.sydney.edu.au/units/ENGG1810/2024-S2C-ND-CC",
    "usyd": "https://www.sydney.edu.au/"
    }

def main():
    web_scrape(urls_to_request["engg1810"])

def web_scrape(website_url: str):
    # This makes a request to the website and stores all the information
    # in the response object. 
    try:
        with req.urlopen(website_url) as response:
            # We can then iterate through the response object
            for line in response:
                # Allowing us to get the byte representation of the website
                # We then decode it from bytecode to python strings
                line: str = line.decode()
                # And finally print out each line
                print(line, end = "")
    except err.URLError as error:
        print(f"Could not open URL: {error}")
        exit(0)

if __name__ == "__main__":
    main()