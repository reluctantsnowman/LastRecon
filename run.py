from config.sites import SITES
from scrapers.shopify_scraper import scrape_shopify


def main():

    print("LastRecon starting...\n")

    for site_name, config in SITES.items():

        print(f"Scraping {site_name}...")

        boots = scrape_shopify(
            config["base"],
            config["collection"]
        )

        print(f"Found {len(boots)} products\n")


if __name__ == "__main__":
    main()