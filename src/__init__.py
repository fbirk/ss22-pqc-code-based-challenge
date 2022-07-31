from input_reader import Reader

# call: python .\__init__.py
def main():
    r = Reader(10)

    print("Read Input...")
    r.readInput()

    print("Done.")

if __name__ == "__main__":
    main()