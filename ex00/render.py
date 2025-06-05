import sys
import os
import re

def main():
    if len(sys.argv) != 2:
        sys.exit( "Error in the args")

    the_dict = {}

    with open('settings.py', 'r', encoding='utf-8') as seti:
        for line in seti :
            line = line.strip()
            if not line or '=' not in line:
                continue
            key, value = line.split('=', 1)
            the_dict[key.strip()] = value.strip()

    with open(sys.argv[1], 'r', encoding='utf-8') as file, \
        open("result.html", 'w', encoding='utf-8') as outfile:
        for line in file:
            for key, value in the_dict.items():
                placeholder = '{' + key + '}'
                if placeholder in line:
                    line = line.replace(placeholder, value)
            outfile.write(line)

if __name__ == "__main__":
    main()