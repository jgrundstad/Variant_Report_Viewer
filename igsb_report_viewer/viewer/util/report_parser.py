__author__ = 'Jason Grundstad'
from django.conf import settings
import json, simplejson
import os
import tablib


def add_goodies(atoms, headers, md_anderson_genes):
    for i in range(0, len(headers)):
        if not atoms[i]:
            atoms[i] = ''
        # highlight NON_SYNONYMOUS_CODING
        if(headers[i] == 'effect' and
                   atoms[i] == 'NON_SYNONYMOUS_CODING'):
            atoms[i] = "<font color=green>%s</font>" % atoms[i]
        # add MDAnderson link to appropriate gene names
        if (headers[i] == 'gene') and (atoms[i] is not None) and (
                    atoms[i].lower() in md_anderson_genes):
            new_link = '{gene}<br><font size=-2><a href={link}>MDAnderson' + \
                           '</a></font>'
            atoms[i] = new_link.format(
                link=md_anderson_genes[atoms[i].lower()],
                gene=atoms[i])
    return atoms


def json_from_report(filename):
    print "%s - creating json from: %s" % (os.getcwd(), filename)
    report_file = open(filename, 'r')
    header_line = report_file.readline().strip()
    splitby = ','
    if '\t' in header_line:
        splitby = '\t'
    cols = header_line.split(splitby)

    with open(settings.LINKS_OUT + 'mdanderson.json', 'r') as md_f:
        md_anderson_genes = json.loads(json.load(md_f))

    d = []

    for line in report_file:
        # remove '%' character to allow numerical sorting on pct columns
        line = line.replace('%', '')
        tokens = line.rstrip('\n').split(splitby)
        formatted_line = add_goodies(tokens, cols, md_anderson_genes)
        d.append(formatted_line)
    data = tablib.Dataset(*d, headers=cols)
    return data
