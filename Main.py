from AprioriAlgorithm import Apriori


def take_input():
    support = input("Please enter the minimum support value in percentage: ")
    confidence = input("Please enter the minimum confidence value in percentage: ")

    return {'support': support, 'confidence': confidence}


def print_output(output):
    print(output)


def __main__():
    user_input = take_input()
    apriori = Apriori()
    output = apriori.run(user_input)
    print_output(output)


__main__()