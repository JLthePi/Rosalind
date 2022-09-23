# SIGN

[ROSALIND | Enumerating Oriented Gene Orderings](https://rosalind.info/problems/sign/)

## **Problem**

A **[signed permutation](https://rosalind.info/glossary/signed-permutation/)** of length nn is some ordering of the positive integers {1,2,…,n} in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4) is a signed permutation of length 5.

**Given:** A positive integer n≤6.

**Return:** The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).

## **Sample Dataset**

```python
2
```

## **Sample Output**

```python
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1
```

## Code

```python
from itertools import permutations, product
from time import time

def SIGN(n: int) -> str:
    isNatural = list(product([-1, 1], repeat=n))
    permutation = list(permutations(range(1, n + 1)))
    count = len(isNatural) * len(permutation)
    res = []

    for nums in permutation:
        for combi in isNatural:
            multi = list(map(lambda x, y: str(x * y), nums, combi))
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

```

## Input

```python
6

```

## Output

```python
46080
-1 -2 -3 -4 -5 -6
-1 -2 -3 -4 -5 6
-1 -2 -3 -4 5 -6
-1 -2 -3 -4 5 6
...
6 5 4 3 -2 -1
6 5 4 3 -2 1
6 5 4 3 2 -1
6 5 4 3 2 1
```

```python
# with printing the result
--- 2.7050 seconds ---

# without printing the result
--- 0.0900 seconds ---
```

## Other Code

```python
def SIGN(n: int) -> str:
		res = ""
    lst = [x for x in permutations([i for i in range(-n,n+1) if (i != 0)], n) if set(range(1, n+1)) == set(map(abs,x))]

    res += f"{len(lst)}\n"
    for i in lst:
        res += f'{" ".join(map(str,i))}\n'
    return res
```

```python
# n = 7

# My code
--- 1.9390 seconds ---

# Code with high Rosalind votes
--- 18.5191 seconds ---
```