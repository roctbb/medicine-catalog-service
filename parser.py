from bs4 import BeautifulSoup
import requests
from time import time
import threading
from sql_logik import create_database
from logger import Logger

save = []


def page_count(url: str) -> int:
    starte = time()
    page = requests.get(url)

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        try:
            last = soup.findAll('span', class_='last')[0]
            count = int(last.findAll("a")[0]["href"].split("?")[1].split("=")[1])
        except:
            count = 1
        finish = time() - starte
        return count
    else:
        raise ConnectionRefusedError


def get_names_and_owners(url: str, pages: int, is_parse_all: bool = False) -> list:
    data = []
    for j in range(1, pages + 1):
        link = url + f"?p={str(j)}"
        last_name = ""
        page = requests.get(link)

        if page.status_code == 200:
            soup = BeautifulSoup(page.text, "html.parser")
            names_g = soup.findAll('td', class_='products-table-name')
            own_g = soup.findAll('td', class_='products-table-company')
            for i in range(len(own_g)):
                if not is_parse_all:
                    if last_name != names_g[i].text.strip():
                        href = names_g[i].findAll("a", class_="no-underline")[0]["href"]
                        # print(href)
                        name = names_g[i].text.strip()
                        own = own_g[i].get_text(" ", strip=True)
                        ap = {"name": name,
                              "name_l": name.lower(),
                              "owner": own,
                              "href": href}
                        data.append(ap)
                        last_name = names_g[i].text.strip()
                else:
                    href = names_g[i].findAll("a", class_="no-underline")[0]["href"]
                    # print(href)
                    name = names_g[i].text.strip()
                    own = own_g[i].get_text(" ", strip=True)
                    ap = {"name": name,
                          "owner": own,
                          "href": href}
                    data.append(ap)
        else:
            print(url, "Erroor")
            raise ConnectionRefusedError
    return data


def add_data(data: list, base_site: str) -> list:
    for i in data:
        bib = []
        href = base_site + i["href"]
        page = requests.get(href)
        if page.status_code == 200:
            soup = BeautifulSoup(page.text, "html.parser")
            bip = soup.findAll("div", id="atc_codes")
            if len(bip)>0:
                i["atx"] = bip[0].findAll("span", class_="block-content")[0].get_text(" ", strip=True)
            info = soup.findAll("div", class_="more-info")
            if len(info) > 0:
                info = info[0].findAll("div", class_="block")
                for k in info:
                    bib.append(k["id"])
                    #print(k)
                #print(bib)
                for z in bib:
                    case = soup.findAll("div", id=z)
                    if case != None and len(case) != 0:
                        case = case[0]
                        # print(case)
                        case = case.findAll("div", class_="block-content")
                        dobi = []
                        for j in case:
                            # print(j)
                            dobi.append(j.get_text(" ", strip=True))
                        i[z] = ' '.join(dobi)
    return data


def start(url: str, base_site: str, loger):
    global save
    loger.info(f"Start on {url}")
    start = time()

    pages = page_count(url)
    pag_c = time() - start
    loger.info(f"Get page count{pages} on {url} at {pag_c}")

    data = get_names_and_owners(url, pages)
    get_list_time = time() - start
    midle = time()
    loger.info(f"Create first part data on {url} at {get_list_time}")

    data = add_data(data, base_site)
    all_time = time() - start
    from_last = time() - midle
    loger.info(f"Create second part data on {url} at {from_last}")
    loger.info(f"All created on {url} at {all_time}")

    for i in data:
        save.append(i)

    #print(save)


if __name__ == "__main__":
    url = [
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-a', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-b', "page": 15},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-v', "page": 11},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-g', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-d', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-e', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-zh', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-z', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-i', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-j', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-k', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-l', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-m', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-n', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-o', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-p', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-r', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-s', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-t', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-u', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-f', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-h', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-ts', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-ch', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-sh', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-eh', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-yu', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/rus-ya', "page": 25},
        {"link": 'https://www.vidal.ru/drugs/products/p/5', "page": 25},
        {"link": "https://www.vidal.ru/drugs/products/p/9", "page": 25}]
    base_site = "https://www.vidal.ru"

    save_directory = "pop/"

    threads = []

    log = Logger("pars.log")

    for i in url:
        read = threading.Thread(target=start, args=(i["link"], base_site, log))
        read.start()
        threads.append(read)

    for thread in threads:
        thread.join()

    log.info(f"We parsed {len(save)} med")
    log.info("Start save")
    create_database(save, "data.db")
    log.info("Save succses")
