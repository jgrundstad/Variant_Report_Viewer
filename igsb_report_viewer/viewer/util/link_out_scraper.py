__author__ = 'Jason Grundstad'
from django.conf import settings
from bs4 import BeautifulSoup
import json
import requests
import re


MD_ANDERSON_URL = 'https://pct.mdanderson.org'
MD_ANDERSON_OUTFILE = settings.LINKS_OUT + 'mdanderson.json'


def merge_dicts(x, y):
    """

    :rtype : dict
    """
    z = x.copy()
    z.update(y)
    return z


def find_mdanderson_genes(soup):
    """

    :rtype : dict
    """
    gene_list = dict()

    # grab all available genes on this page and store links
    gene_urls = soup.find_all('a')
    for gene_url in gene_urls:
        try:
            gene_match = re.match(r'/genes/(.+)/show$', gene_url.get('href'))
            if gene_match:
                gene = gene_match.group(1)
                gene_list[gene] = "{}/genes/{}/show".format(MD_ANDERSON_URL,
                                                            gene)
        except TypeError:
            print "Ran into a None value when parsing gene urls"
    return gene_list


def find_mdanderson_next_page(soup):
    page = None
    page_urls = soup.find_all('a', {'rel': 'next'})
    if len(page_urls) > 0:
        for page_url in page_urls:
            page_match = re.match(r'/genes\?page=(\w+)$', page_url.get('href'))
            if page_match:
                page = page_match.group(1)
            else:
                page = None
    else:
        page = None

    return page


def grab_mdanderson():
    """

    :rtype : dict
    """
    page = 1
    gene_list = dict() # name: url
    while page:
        print "Looking for page: {}".format(page)
        md_url = "https://pct.mdanderson.org/genes?page={}".format(page)
        soup = BeautifulSoup(requests.get(md_url).text)

        # find genes on this page
        page_gene_list = find_mdanderson_genes(soup)
        gene_list = merge_dicts(gene_list, page_gene_list)

        # is there another page to pull from
        page = find_mdanderson_next_page(soup)

    # dump gene_list dict to json file for report_parser.py to grab
    gene_list_json = json.dumps(gene_list)
    with open(MD_ANDERSON_OUTFILE, 'w') as f:
        json.dump(gene_list_json, f)


def main():
    grab_mdanderson()


if __name__ == '__main__':
    main()