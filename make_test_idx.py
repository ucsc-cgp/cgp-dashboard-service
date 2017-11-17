#!/usr/bin/env python

import uuid
import json
import random


def main():
    """Use a template JSONL input file containing donor information,
    copy the first two lines. The first line contains the index, 
    and the second line contains meta data. 
    Create _n_ copies of those two lines, where _n_ is a random 
    number of 9,999 < 1,000,001, and write into a new file.
    MK, 2017-11-14"""

    fname = './test/fb_index.jsonl'

    data_in = []  # declare list
    data_in = read_jsonl(data_in, fname)
    # print("First two lines: {}".format(data_in))

    parsed2 = json.loads(data_in.pop())  # load string method
    parsed1 = json.loads(data_in.pop())

    n = random.randint(9999, 12001)
    data_out = create_jsonl(parsed1, parsed2, n)

    print json.dumps(data_out, indent=4, sort_keys=True)

    with open('fb_index_large.jsonl', 'w') as outfile:
        json.dump(data_out, outfile)


def create_jsonl(parsed1, parsed2, n):
    """ """
    data_out = []
    parsed1['index']['_id'] = 0  # to initiate count to zero
    # Change values in JSON file:
    (parsed1, parsed2) = put_newvals(parsed1, parsed2)
    i = 0
    assert isinstance(n, object)
    while i < n:
        # Set new ID:
        parsed1['index']['_id'] += 1

        # Set new UUIDs:
        parsed2['donor'] = str(uuid.uuid1())
        parsed2['file_id'] = str(uuid.uuid1())

        data_out.append(json.dumps(parsed1))
        data_out.append(json.dumps(parsed2))

        i += 1

    return data_out


def put_newvals(parsed1, parsed2):
    # New ID:
    parsed1['index']['_id'] += 1

    # Set new UUIDs:
    parsed2['donor'] = str(uuid.uuid1())
    parsed2['file_id'] = str(uuid.uuid1())

    return parsed1, parsed2


def read_jsonl(data, fname):
    """Read first two lines of a JSON file named
    fname into a list, data, and return it."""
    with open(fname, 'r') as f:
        data.append(''.join(f.readline()))
        data.append(''.join(f.readline()))
    return data


if __name__ == "__main__":
    # print("   a random UUID:")
    main()
