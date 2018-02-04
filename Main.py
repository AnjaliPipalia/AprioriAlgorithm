import csv

from AprioriAlgorithm import Apriori


def read_file(file_name):
    dataset = list()
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dataset.append(row)
    return dataset


def take_input():
    support = input("Please enter the minimum support value in percentage: ")
    confidence = input("Please enter the minimum confidence value in percentage: ")
    dataset = read_file("dataset_1.csv")
    return {'support': support, 'confidence': confidence, 'dataset': dataset}


def print_output(output):
    print(output)


def __main__():
    user_input = take_input()
    apriori = Apriori()
    output = apriori.run(user_input)
    print_output(output)


__main__()