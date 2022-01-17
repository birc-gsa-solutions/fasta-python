import argparse
import sys
from fasta import parse_fasta


def main():
    argparser = argparse.ArgumentParser(
        description="Extract sub-sequences from a Simple-FASTA file"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    argparser.add_argument(
        "coords",
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin
    )
    args = argparser.parse_args()

    recs = parse_fasta(args.fasta)
    args.fasta.close()

    for line in args.coords:
        name, start, stop = line.split()
        start, stop = int(start), int(stop)
        print(recs[name][start-1:stop-1])
    args.coords.close()


if __name__ == '__main__':
    main()
