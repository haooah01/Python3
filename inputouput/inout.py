"""Serialize and deserialize data using pickle while performing basic file I/O."""

from pathlib import Path
import pickle

BASE_DIR = Path(__file__).parent
BINARY_PATH = BASE_DIR / "binary.dat"
TEXT_PATH = BASE_DIR / "text.txt"


def main():
    mylist = ["This", "is", 4, 13327]

    with open(BINARY_PATH, "wb") as myfile:
        pickle.dump(mylist, myfile)

    with open(TEXT_PATH, "w", encoding="utf-8") as myfile:
        myfile.write("This is a sample string")

    with open(TEXT_PATH, "r", encoding="utf-8") as myfile:
        print(myfile.read())

    with open(BINARY_PATH, "rb") as myfile:
        loadedlist = pickle.load(myfile)
    print(loadedlist)


if __name__ == "__main__":
    main()
