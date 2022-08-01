import sys
from input_reader import Reader

# call: python .\__init__.py
def main():
    inputSize = 10

    if (sys.argv.count > 1):
        inputSize = int(sys.argv[1])

    r = Reader(inputSize)

    print("Read Input...")
    params = r.readInput()
    # params.info()

    print("Done.")

if __name__ == "__main__":
    main()