#! /usr/bin/python


# description...

import sys
import re
import shutil
import tempfile


with open(sys.argv[1], 'rb') as file:
    newfile = tempfile.NamedTemporaryFile(delete=False)
    for line in file:
        if line[4] != "x":
            newline = re.findall("[a-z]+\_[0-9]+\.[a-z]+\.[0-9]+", line)[0]
            newline = str(newline + '\n')
            newfile.write(newline)
        else: 
            continue
    file.close()
    shutil.move(newfile.name, sys.argv[2])
    newfile.close()


