import os
import re

filename_list = os.listdir()
regex = re.compile(r"^(.*)\.(md|markdown)$")
filename_list = [ filename for filename in filename_list if regex.match(filename) ]

for filename in filename_list:
    os.system("pandoc %s -o %s.rst" % (filename, regex.sub(r"\1", filename)))
    
