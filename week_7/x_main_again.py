
# Is this a script or a module?
def main():
    print(what_is_this())

def what_is_this() -> str:
    return "Is this file a script or a module?"

if __name__ == "__main__":
    main()