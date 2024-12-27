# This is a module that is able to be run like a script

def main():
    print(sum(10, 3))

def function_in_inner_module() -> float:
    return "This is a function inside a module inside a package"

if __name__ == "__main__":
    main()