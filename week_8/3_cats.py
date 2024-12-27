from x_cats import Cat # Importing the class Cat

def main():
    # Let's imagine we didn't know we created it
    # Let's just imagine we have a 
    many_cats: list[Cat] = []
    many_cats.append(Cat("Seb", 6))
    many_cats.append(Cat("Misha", 5))
    many_cats.append(Cat("Floyd"))
    many_cats.append(Cat("Matt", 1))

    print("All the cats will now meow")
    for cat in many_cats:
        print(cat.name)
        cat.meow()

    print("Let's kill the cats")
    for cat in many_cats:
        cat.kill()
    
    for cat in many_cats:
        print(cat.name)
        cat.meow()
    
    print("Death to them all!")
    all_dead: bool = False
    while not all_dead:
        all_dead: bool = True
        for cat in many_cats:
            cat.kill()
            if cat.no_lives > 0:
                all_dead: bool = False
    
    for cat in many_cats:
        print(cat.name)

if __name__ == "__main__":
    main()