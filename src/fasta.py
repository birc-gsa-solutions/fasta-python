import typing


def parse_fasta(f: typing.TextIO) -> dict[str, str]:
    """Read a (Simple-)FASTA file and put it in a dictionary."""
    res: dict[str, str] = {}
    for recs in f.read().split('>')[1:]:
        header, *seqs = recs.split('\n')
        res[header.strip()] = "".join(seqs)
    return res
