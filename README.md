# FASTA parser exercises

Genome sequences are usually stored in so-called [FASTA files](https://en.wikipedia.org/wiki/FASTA_format), and we will use the same in this class. However, we will not need to full specification of this file format, since genomic data is commonly stored in files that do not use the full set of features.

The subset of of the FASTA format that we will support, we can call it *Simple-FASTA*, can handle all the genomic data set that I have ever seen, but not the data that some protein data bases will export. We don't need those, however, and there is no need to support it for this class. (You can always implement the full specification some later day, if you feel like it).

Still, we need to handle the Simple-FASTA file format, because we need *some* file format for our input genomes, and we might as well choose one that is likely to work with any real-world data we are likely to encounter.

Therefore, you need to write a parser for Simple-FASTA.

In the projects, you will always get your genomic input in Simple-FASTA files. The exercises below should assist you in writing such a parser and test that it works as intended.

## The Simple-FASTA format

A Simple-FASTA file is a plain text file that consists of one or more records, where each record starts with a `>` as the first character on a line. The first line in a record, the line that starts with `>` is the *header* and the remaining lines contain the sequence.

In a regular FASTA file, the header can contain various meta-information about a sequence, but in Simple-FASTA, it will just be the name of the sequence. You get this name by removing the `>` character and any leading or trailing white-space. So, if the header is `> foo `, then the name is just `foo`, not `> foo `, and not `>foo`. Just `foo`.

The sequence is all the lines that follow the header, until we either see a new header, recognisable by a `>` at the beginning of a line, or the end of the file. Newlines are not considered part of the sequence, so you should remove those and concatenate the lines.

For example, if we have the header

```
> foo
acgtacgt
acgtacgt
```

the the name of the sequence is `foo` and the sequence is `acgtacgtacgtacgt`.

If the Simple-FASTA file looks like this:

```
> foo
acgt
acgt
>bar
tgcatg
ca
```

then there are two records, the first has the name `foo` and sequence `acgtacgt` and the second has the name `bar` and the sequence `tgcatgca`.

## Exercise: Extracting records

Write a program, `fasta-recs`, that takes a Simple-FASTA file as input and outputs one record per line, with the header followed by a tab and then the sequence.

