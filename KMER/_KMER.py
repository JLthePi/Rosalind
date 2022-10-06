import sys
import os
from time import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from _tools.fasta2list import fasta2list


def KMER(data: list) -> str:
    base = ["A", "C", "G", "T"]
    combis = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for m in range(4):
                    combis.append(base[i] + base[j] + base[k] + base[m])

    (fasta, _) = fasta2list(data)
    fasta_dict = dict.fromkeys(combis, 0)

    for i in range(len(fasta[0]) - 3):
        composition = fasta[0][i: i + 4]
        fasta_dict[composition] += 1

    return " ".join(list(map(lambda s: str(fasta_dict[s]), combis)))


if __name__ == "__main__":
    time_start = time()

    with open("rosalind_kmer.txt", "r") as f_in:
        d_in = f_in.readlines()

    d_out = KMER(d_in)
    print(d_out)

    with open("rosalind_kmer_ans.txt", "w") as f_out:
        f_out.write(d_out)

    print(f"--- {time() - time_start:.4f} seconds ---")
