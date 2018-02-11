from itertools import combinations


def more_than_equal_to_min_support(frequency, support, no_of_transactions):
    return ((frequency / no_of_transactions) * 100) >= support


def generate_frequent_itemsets(candidate_itemsets, support, no_of_transactions):
    freq_items = list()
    for item, frequency in candidate_itemsets.items():
        if more_than_equal_to_min_support(frequency, support, no_of_transactions):
            freq_items.append(item)
    return freq_items


def generate_candidate_itemsets(transactions, itemset):
    candidate_itemsets = {}
    for items in itemset:
        freq = 0
        for transaction in transactions:
            if set(items).issubset(set(transaction)):
                freq += 1
        candidate_itemsets[",".join(str(x) for x in items)] = freq
    return candidate_itemsets


def join(frequent_itemsets, size):
    itemsets = set()
    for itemset in frequent_itemsets:
        items = itemset.split(",")
        for item in items:
            itemsets.add(item)
    output = list(combinations(itemsets, size))
    return output


class Apriori():

    def run(self, support, confidence, transactions, items):
        candidate_itemsets = {}
        frequent_itemsets = list()

        for i in range(len(items)):
            temp = generate_candidate_itemsets(transactions, items)
            frequent_itemsets = generate_frequent_itemsets(temp, support, len(transactions))
            items = join(frequent_itemsets, i+2)
            candidate_itemsets = {**candidate_itemsets, **temp}
            if not items:
                break
        return frequent_itemsets
