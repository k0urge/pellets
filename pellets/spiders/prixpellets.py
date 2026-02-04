import ast
import csv
import re
from datetime import datetime

import scrapy
from bs4 import BeautifulSoup

DATA_PATH = 'data/monthly_prices.csv'

month_mapping = {
    "janv.": "Jan",
    "févr.": "Feb",
    "mars": "Mar",
    "avril": "Apr",
    "mai": "May",
    "juin": "Jun",
    "juil.": "Jul",
    "août": "Aug",
    "sept.": "Sep",
    "oct.": "Oct",
    "nov.": "Nov",
    "déc.": "Dec",
}


class PrixpelletsSpider(scrapy.Spider):
    name = "prixpellets"

    def start_requests(self):
        url = "https://www.pelletpreis.ch/fr/price/"
        # url = "https://www.prixpellets.ch/fr/prix/evolution"
        yield scrapy.Request(url)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")

        scripts = soup.find_all('script', type='text/javascript', src=False)

        for script in scripts:
            script_content = script.get_text()
            pattern = r'data\.addRows\((.*?)\);'
            data_match = re.search(pattern, script_content)
            if data_match:
                data_rows = data_match.group(1)
                rows = ast.literal_eval(data_rows)

                with open(DATA_PATH, 'r', newline='', encoding='utf-8') as csv_file_input:
                    data = [row for row in csv.reader(csv_file_input)]

                for row in rows:
                    for month_fr, month_en in month_mapping.items():
                        row[0] = row[0].replace(month_fr, month_en)
                    row[0] = datetime.strptime(row[0], "%b %Y").strftime("%Y-%m")
                    if row[0] not in [a[0] for a in data]:
                        data.append(row)

                with open(DATA_PATH, 'w', newline='', encoding='utf-8') as csv_file_output:
                    csv_writer = csv.writer(csv_file_output)
                    for row in data:
                        csv_writer.writerow(row)
                break
