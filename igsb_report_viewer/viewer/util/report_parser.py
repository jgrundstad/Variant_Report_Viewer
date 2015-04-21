__author__ = 'jgrundst'
import os
from collections import defaultdict


def json_from_report(filename):
    print "%s - creating json from: %s" % (os.getcwd(), filename)
    report_file = open(filename, 'r')
    content = defaultdict()
    header_line = report_file.readline()
    cols = header_line.split()
    data = []
    for line in report_file:
        line.rstrip()
        data.append(line.split())


    return content
