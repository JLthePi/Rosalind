from itertools import permutations, product
from time import time


def SIGN(n: int) -> str:
    signs = list(product([-1, 1], repeat=n))
    perms = list(permutations(range(1, n + 1)))
    count = len(signs) * len(perms)
    res = []

    for perm in perms:
        for sign in signs:
            multi = list(map(lambda x, y: str(x * y), perm, sign))
            res.append(multi)

    return f"{count}\n"+"\n".join(map(lambda s: " ".join(s), res))


if __name__ == "__main__":
    time_start = time()

    with open("rosalind_sign.txt", "r") as f_in:
        d_in = int(f_in.read())

    d_out = SIGN(d_in)
    print(d_out)

    with open("rosalind_sign_ans.txt", "w") as f_out:
        f_out.write(d_out)

    print(f"--- {time() - time_start:.4f} seconds ---")
