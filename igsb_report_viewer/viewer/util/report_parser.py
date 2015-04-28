__author__ = 'Jason Grundstad'
from django.conf import settings
import json, simplejson
import os
import tablib


def add_goodies(atoms, headers, md_anderson_genes):
    print "headers: %s\natoms: %s" % (headers, atoms)
    for i in range(0, len(headers)):

        if(headers[i] == 'effect' and
                   atoms[i] == 'NON_SYNONYMOUS_CODING'):
            atoms[i] = "<font color=green>%s</font>" % atoms[i]

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
    cols = report_file.readline().strip().split()

    with open(settings.LINKS_OUT + 'mdanderson.json', 'r') as md_f:
        md_anderson_genes = json.loads(json.load(md_f))

    d = []

    for line in report_file:
        tokens = line.rstrip('\n').split('\t')
        formatted_line = add_goodies(tokens, cols, md_anderson_genes)
        d.append(formatted_line)
    data = tablib.Dataset(*d, headers=cols)
    return data
