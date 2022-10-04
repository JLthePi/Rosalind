from time import time


def DNA(s: str) -> str:
    A, C, G, T = 0, 0, 0, 0

    for char in s:
        if char == "A":
            A += 1
        elif char == "C":
            C += 1
        elif char == "G":
            G += 1
        elif char == "T":
            T += 1

    # A = s.count("A")
    # C = s.count("C")
    # G = s.count("G")
    # T = s.count("T")

    return " ".join(map(str, [A, C, G, T]))


if __name__ == "__main__":
    time_start = time()

    with open("rosalind_dna.txt", "r") as f_in:
        d_in = f_in.readlines()[0].strip()

    d_out = DNA(d_in)
    print(d_out)

    with open("rosalind_dna_ans.txt", "w") as f_out:
        f_out.write(d_out)

    print(f"--- {time() - time_start:.4f} seconds ---")
