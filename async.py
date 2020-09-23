from IPython import embed
from bs4 import BeautifulSoup
import lxml, re, math, aiohttp, asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

def get_listing_urls(resp):
    soup = BeautifulSoup(resp, features="lxml")
    links = [tag["href"] for tag in soup.find_all("a", attrs={"href":re.compile("sc_suginami.*nc_[0-9]*\/\?")})]
    lanks = set([re.search("(.*[0-9](?=\/))", link)[0] for link in links])
    try:
        number_of_hits = math.ceil(int(re.search("[0-9]*(?=件)",soup.find("div", attrs={"class":"pagination_set-hit"}).text)[0])/30)
    except:
        pass
    return({"links":lanks,"number_of_hits":number_of_hits})

def get_distances(resp):
    soup = BeautifulSoup(resp, features="lxml")
    distance_tags = soup.find_all("div", text=re.compile("[0-9]m"))
    distance_texts = [distance_tag.text for distance_tag in distance_tags]
    distance_text_groups = [re.search("(.*)(まで)([0-9]*)(m)", distance_text) for distance_text in distance_texts]
    try:
        distances = [(distance_text_group[1],distance_text_group[3]) for distance_text_group in distance_text_groups]
    except:
        distances = []
    print(distances)
    
async def main():
    listing_urls = []
    for i in range(1,6):
        async with aiohttp.ClientSession() as session:
            print(i)
            resp = await fetch(session, "https://suumo.jp/ikkodate/tokyo/sc_suginami/pnz1{}.html".format(str(i)))
            scrape_results = get_listing_urls(resp)
            listing_urls += scrape_results["links"]
    for listing_url in listing_urls:
        async with aiohttp.ClientSession() as session:
            new_url = "https://suumo.jp{}/kankyo/".format(listing_url)
            resp = await fetch(session, new_url)
            print(new_url)
            get_distances(resp)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())