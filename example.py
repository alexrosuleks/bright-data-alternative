"""Amazon Product Scraper with the Scrapely Python SDK (scrapely-client-python).

Install: pip install scrapely-client-python
Run:     SCRAPELY_TOKEN=your_token python example.py
"""
import json
import os

from scrapely_client import ScrapelyClient


def main() -> None:
    client = ScrapelyClient(os.environ['SCRAPELY_TOKEN'])

    run_input = {
        "categoryOrProductUrls": [
            {
                "url": "https://www.amazon.com/dp/B09X7MPX8L"
            }
        ],
        "maxItemsPerStartUrl": 10,
        "maxSearchPagesPerStartUrl": 0,
        "maxProductVariantsAsSeparateResults": 0,
        "scrapeProductDetails": True,
        "scrapeProductVariantPrices": False,
        "maxOffers": 0,
        "scrapeSellers": False,
        "useCaptchaSolver": False,
        "proxyCountry": "AUTO_SELECT_PROXY_COUNTRY",
        "locationDeliverableRoutes": [
            "PRODUCT",
            "SEARCH",
            "OFFERS"
        ],
        "proxyConfiguration": {
            "useScrapelyProxy": True,
            "scrapelyProxyGroups": [
                "DATACENTER"
            ]
        }
    }

    # Start the scraper on Scrapely and wait for it to finish.
    run = client.actor('shelfbright/amazon-product-scraper').call(run_input=run_input)
    if run is None:
        raise RuntimeError('Run was not found')

    # Read the scraped results from the run's dataset.
    items = list(client.dataset(run.default_dataset_id).iterate_items())
    print(f'Scraped {len(items)} results')
    print(json.dumps(items, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
