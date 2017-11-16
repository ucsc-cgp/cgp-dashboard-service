#!/usr/bin/env python

import uuid
import json
import random


def main():
    """Use a JSONL input file containing donor information, copy the
    first two lines. The first line contains the index, and the 
    second line contains meta data. 
    Create a copy of the two lines N times, where N is a number 
    > 9,999, and write into a new file.
    MK, 2017-11-14"""
    
    #print(uuid.uuid4())
    fname = './test/fb_index.jsonl'

    data_in = []  # declare list
    data_in = read_jsonl(data_in, fname)
    #print("First two lines: {}".format(data_in))

    parsed2 = json.loads(data_in.pop())  # load string method
    parsed1 = json.loads(data_in.pop())

    data_out = []
    N = 3 #random.randint(9999, 1000001)
    data_out = create_JSONL(data_out, parsed1, parsed2, N)
    
    # Change values in JSON file:
    #(parsed1, parsed2) = put_newvals(parsed1, parsed2)

    # Some form of pretty-print:
    #print json.dumps(parsed1, indent=4, sort_keys=True)
    #print json.dumps(parsed2, indent=4, sort_keys=True)

    print json.dumps(data_out, indent=4, sort_keys=True)


def create_JSONL(data_out, parsed1, parsed2, N):
    """ """
    # Change values in JSON file:
    (parsed1, parsed2) = put_newvals(parsed1, parsed2)

    n = 0
    while n < N:
         # New ID: 
         parsed1['index']['_id'] += 1

         # Set new UUIDs:
         parsed2['donor'] = str(uuid.uuid1())
         parsed2['file_id'] = str(uuid.uuid1())

         data_out.append(json.dumps(parsed1))
         data_out.append(json.dumps(parsed2))

         n += 1

    return data_out

         
def put_newvals(parsed1, parsed2):

    # New ID:
    parsed1['index']['_id'] += 1

    # Set new UUIDs:
    parsed2['donor'] = str(uuid.uuid1())
    parsed2['file_id'] = str(uuid.uuid1())

    return parsed1, parsed2

    
def read_jsonl(data, fname):
    """Read first two lines into list data and return it."""
    with open(fname, 'r') as f:
             data.append(''.join(f.readline()))
             data.append(''.join(f.readline()))
    return data


if __name__ == "__main__":
    #print("   a random UUID:")
    main()
 
