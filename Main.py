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
    support = int(input("Please enter the minimum Support value in percentage: "))
    confidence = int(input("Please enter the minimum Confidence value in percentage: "))
    dataset = read_file("dataset_1.csv")
    items = read_file("items.csv")
    return {'support': support, 'confidence': confidence, 'dataset': dataset, 'items': items}


def print_output(output):
    print(output)


def __main__():
    user_input = take_input()
    apriori = Apriori()
    output = apriori.run(user_input['support'], user_input['confidence'], user_input['dataset'], user_input['items'])
    print_output(output)


__main__()