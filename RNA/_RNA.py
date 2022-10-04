from time import time


def RNA(s: str) -> str:
    return s.replace("T", "U")


if __name__ == "__main__":
    time_start = time()

    with open("rosalind_rna.txt", "r") as f_in:
        d_in = f_in.readlines()[0].strip()

    d_out = RNA(d_in)
    print(d_out)

    with open("rosalind_rna_ans.txt", "w") as f_out:
        f_out.write(d_out)

    print(f"--- {time() - time_start:.4f} seconds ---")
