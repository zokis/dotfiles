#!/usr/bin/env python

import os
from random import choice


def main():
    files = []
    for root, dirs, file_names in os.walk(os.environ['HOME']+'/.git_sounds'):
        for file_name in file_names:
            if file_name[-4:] == '.wav':
                files.append(os.path.join(root, file_name))
    print choice(files) if files else ''


if __name__ == '__main__':
    main()
