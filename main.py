class AminoCoder:
    trans_table_path = "transl_table.txt"

    def __init__(self):
        self.transDict = dict()
        with open(self.trans_table_path) as F:
            for l in F.readlines():
                name, codes = l.split(':')
                self.transDict[name.strip()] = codes.strip().split()

    def __generate_sequence(self, amins: list, rest: str):
        if len(amins) == 0:
            yield rest
        else:
            for code in self.transDict[amins[-1]]:
                yield self.__generate_sequence(amins[:-1], code + rest)

    def generate_sequence(self, aminosequence: str):
        amins = []
        for i in range(0, len(aminosequence), 3):
            amins.append(aminosequence[i:i + 3])
        return self.__generate_sequence(amins, '')

    def get_sequence(self, aminosequence: str):
        r = self.generate_sequence(aminosequence)
        gen = type(r)
        results = list(r)
        while type(results[0]) == gen:
            temp = results
            results = []
            [results.extend(x) for x in temp]
        return results


def read_seqence():
    with open("sequence.txt") as input_file:
        sequence = input_file.readline().strip()
    return sequence


def write_results_to_file(a):
    with open("result.txt", "w") as result_file:
        for i in a.get_sequence(sequence):
            result_file.write(i)
            result_file.write("\n")


if __name__ == '_main_':
    sequence = read_seqence()
    a = AminoCoder()
    write_results_to_file(a)
