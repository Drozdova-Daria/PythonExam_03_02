from dir_reader import DirReader
from graph_iterator import GraphIterator


def fill_dict_scientist_scientists(dict_scientist_scientists, scientists):
    if len(scientists) == 2:
        if scientists[0] not in dict_scientist_scientists:
            dict_scientist_scientists[scientists[0]] = list()
        dict_scientist_scientists[scientists[0]].append(scientists[0])
    else:
        for i in range(len(scientists) - 1):
            for j in range(i + 1, len(scientists) - 1):
                if scientists[i] not in dict_scientist_scientists:
                    dict_scientist_scientists[scientists[i]] = []
                dict_scientist_scientists[scientists[i]].append(scientists[j])


def read_lines_in_file(file, dict_scientist_scientists):
    ln = file.readline()
    for line in file.readlines():
        scientists_seq = line.split("\t")
        fill_dict_scientist_scientists(dict_scientist_scientists, scientists_seq)


def fill_scientist_seq_count(dict_scientist_scientists):
    scientist_seq_count = {}
    for science_name, seq_count in GraphIterator(dict_scientist_scientists):
        scientist_seq_count[science_name] = seq_count
    return scientist_seq_count

def main():
    dict_scientist_scientists = {}
    with DirReader("data") as file_names:
        for file in file_names:
            read_lines_in_file(file, dict_scientist_scientists)
    scientist_seq_count = fill_scientist_seq_count(dict_scientist_scientists)
   

main()
