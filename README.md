# Pellets

This project scrapes the latest wood pellet prices from [prixpellets.ch](https://www.prixpellets.ch)
and generates plots to visualize the price evolution.

It also provides a GitHub Pages site to display the plots
at [https://k0urge.github.io/pellets/](https://k0urge.github.io/pellets/).

The project uses [Scrapy](https://scrapy.org/) to scrape the data and [Matplotlib](https://matplotlib.org/) to generate the plots.
Additionally, [Jekyll](https://jekyllrb.com/) is used to create the GitHub Pages site.

## Local Usage
Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate   # on Windows, use .venv\Scripts\activate      
```

Install the required packages:
```bash
pip install -r requirements-scrapy.txt
pip install -r requirements-plot.txt
```

### Scrape Data
To scrape the latest wood pellet prices, run the following command:
```bash
scrapy crawl prixpellets
```
The scraped data will be saved in the `data` directory.

### Generate Plots
To generate the plots, run the following command:
```bash
python plot.py
```
The generated plots will be saved in the `docs/images` directory.
