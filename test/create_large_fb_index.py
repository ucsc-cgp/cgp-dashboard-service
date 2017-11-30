#!/usr/bin/env python

import uuid
import json
import os
from random import randint
import click

"""Test whether `outfile' has expected entries by using
   `cat outfile_name.json | grep -o -P '.donor.{0,20}'` on the
   command line."""


@click.command()
@click.option('--max_idx', default=15000, help='Maximum index.')
def main(max_idx):
    """This generates a mock input file I used for implementing
    paging. The file it generates will have more than 9,999 entries.
    It uses dcc-dashboard-service/test/fb_index.jsonl (relative path)
    as the template JSONL input file and copies the first two lines from it.
    Sets the index of the key "_id" to zero, and generates a random number
    n of samples (each with two lines) counting up.
    n will be a random number in the range between 9,999 and MAXIDX.
    If the that mock file exists already it will overwrite it
    without warning.

    The mock file will have unique values for "index/_id", "donor" and
    "file_id"."""

    fname = './dcc-dashboard-service/test/fb_index.jsonl'
    outfile = './dcc-dashboard-service/test/fb_index_large.jsonl'

    data_in = []  # declare list
    data_in = read_jsonl(data_in, fname)
    # print("First two lines: {}".format(data_in))

    # Get the two last entries from the stack of the file:
    parsed2 = json.loads(data_in.pop())  # load string method
    parsed1 = json.loads(data_in.pop())

    n = randint(9999, max_idx)  # random number of entries in file

    try:
        os.remove(outfile)
    except OSError:
        pass

    create_jsonl(parsed1, parsed2, n, outfile)

    print("Wrote JSONL to {}".format(outfile))


def create_jsonl(parsed1, parsed2, n, outfile):
    print("  \nCreating JSON Lines file ...")
    # Change values in JSON file.
    i = 0
    while i < n:
        # print("i = {}".format(i))
        # Set new index ID:
        parsed1['index']['_id'] = i

        # Set new UUIDs:
        parsed2['donor'] = unicode(str(uuid.uuid1()), "utf-8")
        parsed2['file_id'] = unicode(str(uuid.uuid1()), "utf-8")

        # Append to output file.
        with open(outfile, 'a') as f:
            f.write(json.dumps(parsed1) + '\n')
            f.write(json.dumps(parsed2) + '\n')

        i += 1


def read_jsonl(data, fname):
    """Read first two lines of a JSON file named
    fname into a list, data, and return it."""
    with open(fname, 'r') as f:
        data.append(f.readline())
        data.append(f.readline())
    return data


if __name__ == "__main__":
    main()
