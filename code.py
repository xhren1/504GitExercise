def count_base(seq):
    base_dict = dict()
    for base in seq:
        if base not in base_dict:
            base_dict[base] = 1
        else:
            base_dict[base] += 1
    return base_dict

def count_freq(base_dict):
    print('freqs')
    total = float(sum([base_dict[base] for base in base_dict.keys()]))
    for base in base_dict.keys():
        print(base + ':' + str(base_dict[base]/total))

count_freq(count_base('ATCTGACGCGCGCCGC'))
