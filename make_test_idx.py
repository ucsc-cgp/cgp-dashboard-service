#!/usr/bin/env python

import uuid
import json


def main():
    """Create a JSONL file with donor information, and multiply lines. An odd line in that file contains the instruction for the file rimmdediately below it."""
    #print(uuid.uuid4())
    fname = './test/fb_index.jsonl'

    data = []  # make a list
    data = read_jsonl(data, fname)
    #print("First two lines: {}".format(data))

    parsed2 = json.loads(data.pop())  # load string method
    parsed1 = json.loads(data.pop())

    # Change values in JSON file:
    (parsed1, parsed2) = put_newvals(parsed1, parsed2)
    
    print json.dumps(parsed1, indent=4, sort_keys=True)
    print json.dumps(parsed2, indent=4, sort_keys=True)

def put_newvals(parsed1, parsed2):

    # New ID:
    parsed1['index']['_id'] += 1

    # New donor UUID:
    parsed2['donor'] = str(uuid.uuid4())  # random UUID

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
 
