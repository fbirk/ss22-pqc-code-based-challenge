import sys
from input_reader import Reader

# call: python .\__init__.py
def main():
    inputSize = 10
    message = ""

    if (sys.argv.count > 1):
        inputSize = int(sys.argv[1])
    
    if (len(sys.argv) > 2):
        message = sys.argv[2]


    r = Reader(inputSize)

    print("Read Input...")
    params = r.readInput()
    # params.info()

    print("Done.")

if __name__ == "__main__":
    main()