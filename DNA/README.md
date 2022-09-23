# DNA

[ROSALIND | Counting DNA Nucleotides](https://rosalind.info/problems/dna/)

## **Problem**

A **[string](https://rosalind.info/glossary/string/)** is simply an ordered collection of symbols selected from some **[alphabet](https://rosalind.info/glossary/alphabet/)** and formed into a word; the **[length](https://rosalind.info/glossary/string-length/)** of a string is the number of symbols that it contains.

An example of a length 21 **[DNA string](https://rosalind.info/glossary/dna-string/)** (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

**Given:** A DNA string s of length at most 1000 nt.

**Return:** Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

## **Sample Dataset**

```python
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
```

## **Sample Output**

```python
20 12 17 21
```

## Code

```python
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

```

## Input

```python
CGCAATAGAATTAACTCGGCTAATTATCAGAGTTAGTCACCGTCGAACGCGACGTTGTGCCATGGGGAAGTCTGTCTCGCAACATGGATGTGTACCCTCGATCTAATGGGTATGTCAGTGCTCGAGCGTGTCTTTGATGCACGAAAAACCGTCGAGTAAGCTTAGATCAAATTGGGAACCCACACCGCCTGGGCAGATATGAAGAGTCCGTATTAACACTTAGCGGCGGAGCGAATAGCCATCGCCGATCACATTGGATATTGTTCTTGCGAGAATATCATGATATTGAAAAGACGACTCGAACTGTACCTGCATTCCCAGAGGGAGCGCGGAACAACGCGAAGTATGAATCCACATAAACAAATCTTACTTGTTGAATGTAGAGCGGTGCTAGGGATTAGTATCTCATCAAGGTCGCGCTGTCAACGAATGTACAGAGCGCCACAGGTTTGAAACACTAGCACAGTGCTTGCAGCGCGCGAAAGGGGCTGACATCAGAAAGTCATGACTCTGTGCCAAGTAAAGGTTGCCCATGGTTAACTCGTGAGACCAATCAAAGAACTCCCGAAAGGGAGCCCGTTTGCTGCACCAACATAGGTGTCTATTTATCATTGCTCCGTGAGTAATGAAGGCGACCTTACTCGCTGCATGACCACCGAGCTCGTAAGCAAGGTTGTCTACGAATATATTCTCAGTGAGTGTTTCAGAAACAGCTAACGGATGTACCAGTTAGAGATCATGGAAGCATCTCCACACACCGCCGGGCCAGCTCACCACGGTCTAGAAGAACTGAGCAGATTTTGAGCAGTTTGTAAGGAGAAAT

```

## Output

```python
238 187 208 190
```
```python
--- 0.0010 seconds ---
```

## Other Code

```python
def DNA(s: str) -> str:
    A, C, G, T = 0, 0, 0, 0

		A = s.count("A")
		C = s.count("C")
		G = s.count("G")
		T = s.count("T")
	
    return " ".join(map(str, [A, C, G, T]))

```

```python
# len(s) = 10000000

# s를 순회하는 방법
2891831 2272229 2527388 2308551
--- 0.7820 seconds ---

# s.count를 사용한 방법
2891831 2272229 2527388 2308551
--- 0.0870 seconds ---

# count를 사용하는 것이 더 빠르다
```