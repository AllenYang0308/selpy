#!/usr/bin/env python

import tarfile

def extract(filename, mode, distination, labal=""):
    tar = tarfile.open(filename, mode)
    tar.extractall(path=distination)

if __name__ == '__main__':

    extract("firefox-71.0.tar.bz2", "r:bz2", "/tmp/", "Binary")
    extract("geckodriver-v0.26.0-linux64.tar.gz", "r:gz", "/tmp/", "Driver")

