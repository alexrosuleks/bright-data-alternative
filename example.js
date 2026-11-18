// Amazon Product Scraper with the Scrapely JavaScript SDK (scrapely-client).
// Install: npm install scrapely-client
// Run:     SCRAPELY_TOKEN=your_token node example.js
const { ScrapelyClient } = require('scrapely-client');

const client = new ScrapelyClient({ token: process.env.SCRAPELY_TOKEN });

async function main() {
    const input = {
        "categoryOrProductUrls": [
            {
                "url": "https://www.amazon.com/dp/B09X7MPX8L"
            }
        ],
        "maxItemsPerStartUrl": 10,
        "maxSearchPagesPerStartUrl": 0,
        "maxProductVariantsAsSeparateResults": 0,
        "scrapeProductDetails": true,
        "scrapeProductVariantPrices": false,
        "maxOffers": 0,
        "scrapeSellers": false,
        "useCaptchaSolver": false,
        "proxyCountry": "AUTO_SELECT_PROXY_COUNTRY",
        "locationDeliverableRoutes": [
            "PRODUCT",
            "SEARCH",
            "OFFERS"
        ],
        "proxyConfiguration": {
            "useScrapelyProxy": true,
            "scrapelyProxyGroups": [
                "DATACENTER"
            ]
        }
    };

    // Start the scraper on Scrapely and wait for it to finish.
    const run = await client.actor('shelfbright/amazon-product-scraper').call(input);

    // Read the scraped results from the run's dataset.
    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    console.log(`Scraped ${items.length} results`);
    console.log(JSON.stringify(items, null, 2));
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
