def more_than_equal_to_min_support(frequency, support, no_of_transactions):
    return ((frequency / no_of_transactions) * 100) >= support


def generate_frequent_itemsets(candidate_itemsets, support, no_of_transactions):
    freq_items = list()
    for item, frequency in candidate_itemsets.items():
        if more_than_equal_to_min_support(frequency, support, no_of_transactions):
            freq_items.append(item)
    return freq_items


def generate_candidate_itemsets(transactions):
    candidate_itemsets = {}
    for transaction in transactions:
        for item in transaction:
            if item not in candidate_itemsets:
                candidate_itemsets[item] = 1
            else:
                candidate_itemsets[item] += 1
    return candidate_itemsets


class Apriori():

    def run(self, support, confidence, transactions):
        candidate_itemsets = generate_candidate_itemsets(transactions)
        frequent_itemsets = generate_frequent_itemsets(candidate_itemsets, support, len(transactions))
        return frequent_itemsets
