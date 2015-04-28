from ..util import link_out_scraper


#def run_cron_test():
#    f = open(settings.LINKS_OUT + '/test_file.txt', 'a')
#    print >>f, "testing, yo"


def gather_md_anderson():
    link_out_scraper.grab_mdanderson()