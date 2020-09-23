import urllib.request as ur
from bs4 import BeautifulSoup
from IPython import embed
import lxml, re, math

def get_links(url,ward):
    resp = ur.urlopen(url)
    soup = BeautifulSoup(resp, features="lxml")
    links = [tag["href"] for tag in soup.find_all("a", attrs={"href":re.compile("sc_{}.*nc_[0-9]*\/\?".format(ward))})]
    lanks = set([re.search("(.*[0-9](?=\/))", link)[0] for link in links])
    try:
        number_of_hits = math.ceil(int(re.search("[0-9]*(?=件)",soup.find("div", attrs={"class":"pagination_set-hit"}).text)[0])/30)
    except:
        pass
    return({"links":lanks,"number_of_hits":number_of_hits})

def get_listings():
    wards = {"setagaya":[], "suginami":[], "meguro":[]}
    for ward in wards:
        base_url = "https://suumo.jp/ikkodate/tokyo/sc_{}/".format(ward)
        scrape_results = get_links(base_url,ward)
        wards[ward] += scrape_results["links"]
        for i in range(1,scrape_results["number_of_hits"]):
            scrape_url = base_url+"pnz1"+str(i)+".html"
            scrape_results = get_links(scrape_url,ward)
            wards[ward] += scrape_results["links"]
        print(ward)
    
listings = get_listings()
embed()
