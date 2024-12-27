from datetime import date

def main():

    print(date)

    now: date = date.today()
    print(type(now))
    print(now)
    print(now.isoweekday())
    print(now.strftime("%m-%d-%y | %A %d %b %Y"))
    
    # It's mah birthday!
    valentines: date = date(2004, 2, 14)
    print(type(valentines))
    print(valentines)
    print(valentines.isoweekday())
    print(valentines.strftime("%m-%d-%y | %A %d %b %Y"))

if __name__ == "__main__":
    main()