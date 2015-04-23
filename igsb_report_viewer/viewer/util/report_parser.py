__author__ = 'Jason Grundstad'
import os
import tablib
import link_out_scraper


MD_ANDERSON_GENES = dict()


def add_goodies(atoms, headers):
    print "headers: %s\natoms: %s" % (headers, atoms)
    global MD_ANDERSON_GENES
    for i in range(0, len(headers)):
        if(headers[i] == 'effect' and
                   atoms[i] == 'NON_SYNONYMOUS_CODING'):
            atoms[i] = "<font color=green>%s</font>" % atoms[i]
        if headers[i] == 'gene' and atoms[i] is not None \
                and atoms[i].lower() in MD_ANDERSON_GENES:
                    atoms[i] = '<a href={link}>{gene}</a>'.format(
                        link=MD_ANDERSON_GENES[atoms[i].lower()],
                        gene=atoms[i])
    return atoms


def json_from_report(filename):
    print "%s - creating json from: %s" % (os.getcwd(), filename)
    report_file = open(filename, 'r')
    cols = report_file.readline().strip().split()
    d = []
    global MD_ANDERSON_GENES
    MD_ANDERSON_GENES = link_out_scraper.grab_mdanderson()
    for line in report_file:
        tokens = line.rstrip('\n').split('\t')
        formatted_line = add_goodies(tokens, cols)
        d.append(formatted_line)
    data = tablib.Dataset(*d, headers=cols)
    return data
