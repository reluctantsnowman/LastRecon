import requests


def build_products_url(base, collection):

    if "?" in collection:
        path = collection.split("?")[0]
    else:
        path = collection

    return f"{base}{path}/products.json?limit=50"


def scrape_shopify(base, collection):

    url = build_products_url(base, collection)

    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
    except Exception as e:
        print(f"Request failed: {e}")
        return []

    data = r.json()
    products = data.get("products", [])

    boots = []

    for product in products:

        variants = product.get("variants", [])

        price = ""
        if variants:
            price = variants[0].get("price", "")

        boots.append({
            "name": product.get("title"),
            "url": f"{base}/products/{product.get('handle')}",
            "price": price
        })

    return boots