#!/bin/env python
import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from colorama import Style
from lxml import etree

URL = "https://www.sospronostics.com/pronostics/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}
RESULTS_FILE = "results"


def load_existing_pronos(results_file: Path):
    # ['04/12/2024 - 20:30', '04/12/2024 - 21:00']
    res = set()
    with results_file.open("r") as f:
        for line in f.readlines():
            data = json.loads(line)
            res.add(data[0])
    return res


webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))

pronos = dom.xpath("//article")

results_file = Path(RESULTS_FILE)
existings_pronos = load_existing_pronos(results_file)
with results_file.open("a", encoding="utf-8") as f:
    for prono in pronos:
        elems = list(
            filter(
                lambda e: e not in ["\n", "-", "Notre prono"], prono.xpath(".//text()")
            )
        )
        elems = elems[:5]
        if elems[0] in existings_pronos:
            print(Style.DIM + str(elems) + Style.RESET_ALL)
        else:
            print(elems)
            line = json.dumps(elems, ensure_ascii=False)
            f.write(f"{line}\n")
