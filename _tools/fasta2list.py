def fasta2list(data: list):
    name = []
    fasta = []

    for line in data:
        if line.startswith(">"):
            name.append(line[1:].strip())
            fasta.append("")
        else:
            fasta[-1] += line.strip()

    return fasta, name
