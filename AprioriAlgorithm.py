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


def get_combinations(itemset):
    output = {}
    items = itemset.split(",")
    for item in items:
        output[item] = [i for i in items if i != item]
    for size in range(2, len(items)):
        keys = list(combinations(items, size))
        for key in keys:
            output[key] = [i for i in items if i not in key]
    return output


def get_support(XY, c_itemsets, transactions):
    xy = XY.split(",")
    xy.sort()
    # print(xy)
    for key, value in c_itemsets.items():
        c_key = key.split(',')
        c_key.sort()
        if c_key == xy:
            return value
    print("OMG")


class Apriori():

    def run(self, support, confidence, transactions, items):

        candidate_itemsets = {}
        frequent_itemsets = list()

        for i in range(len(items)):
            temp = generate_candidate_itemsets(transactions, items)
            temp_frequent_itemsets = generate_frequent_itemsets(temp, support, len(transactions))
            items = join(temp_frequent_itemsets, i + 2)
            candidate_itemsets = {**candidate_itemsets, **temp}
            frequent_itemsets += temp_frequent_itemsets
            if not items:
                break
        for itemset in frequent_itemsets:
            combinations = get_combinations(itemset)
            for X, Y in combinations.items():
                if len(Y) == 0:
                    continue
                strX = X
                strY = ','.join(Y)
                if type(X) == tuple:
                    strX = ','.join(X)
                strXY = strX + ',' + strY
                supportXY = get_support(strXY, candidate_itemsets, transactions)
                supportX = get_support(strX, candidate_itemsets, transactions)
                if (supportXY / supportX)*100 >= int(confidence):
                    print(strX + " ---> " + strY)
        return frequent_itemsets
