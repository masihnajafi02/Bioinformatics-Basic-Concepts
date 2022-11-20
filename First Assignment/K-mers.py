import copy

set_of_kmers = []
all_symbols = []
symbols = input().split()
k = int(input())
for symbol in symbols:
    set_of_kmers.append(symbol)

final_set = copy.deepcopy(set_of_kmers)
for i in range(k - 1):
    set_of_kmers = copy.deepcopy(final_set)
    final_set = copy.deepcopy([])
    for j in set_of_kmers:
        for z in symbols:
            final_set.append(j + z)
            last_set = copy.deepcopy(final_set)
for element in sorted(final_set):
    print(element)
