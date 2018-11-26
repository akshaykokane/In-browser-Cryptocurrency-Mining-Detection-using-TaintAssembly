import sys

def findSimilarPattern(fileName):
    with open('taint_coin_v8.log', 'r') as coinhive:
        with open(fileName, 'r') as file_under_inspection:
            similarPattern = set(coinhive).intersection(file_under_inspection)
    i=0
    with open('same.txt', 'w') as file_out:
        for line in similarPattern:
            file_out.write(line)
            i = i + 1
    return i


def main():
    for arg in sys.argv[1:]:
        i = findSimilarPattern(arg)

    threshold = len(arg)/2

    if i>threshold:
        print("\n\nDANGER: The Website was using InBrowser CryptoCurrency Mining")

    else:
        print("\n\nMESSAGE: The Website was not using InBrowser CryptoCurrency Mining")


if __name__ == "__main__":
    main()

print("\nEnd")