import requests
from bs4 import BeautifulSoup
import json

urls = [
    "https://offtrendclub.eu/sk/products/adidas-yeezy-qntm-hi-res-coral?variant=43688950825182",
    "https://offtrendclub.eu/sk/products/jordan-2-retro-se-nina-chanel-abney-womens?variant=43366672695518",
    "https://offtrendclub.eu/sk/products/adidas-yeezy-bsktbl-knit-slate-blue?variant=43415810638046",
    "https://offtrendclub.eu/sk/products/adidas-yeezy-boost-350-v2-slate?variant=49624829886794",
    "https://offtrendclub.eu/sk/products/jordan-2-retro-sp-union-grey-fog?variant=43366654312670",
    "https://offtrendclub.eu/sk/collections/sneakers/products/nike-zoom-cortez-sp-sacai-white-university-red-blue",
    "https://offtrendclub.eu/sk/collections/sneakers/products/jordan-1-low-og-neutral-grey-2021-womens",
    "https://offtrendclub.eu/sk/collections/sneakers/products/nike-air-max-90-black-anthracite-cool-grey",
    "https://offtrendclub.eu/sk/collections/sneakers/products/jordan-1-mid-yellow-ochre",
    "https://offtrendclub.eu/sk/collections/sneakers/products/new-balance-550-aime-leon-dore-white-navy-red",
    "https://offtrendclub.eu/sk/products/jordan-1-retro-high-og-black-white?variant=49600192184650"
]

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        name = soup.find("h1", class_="product-title").text.strip()
        image = soup.find("div", class_="product__media") \
                    .find("img")["src"]
        variant_id = url.split("variant=")[-1]
        size_div = soup.find("label", {"for": f"SingleOptionSelector-0"})
        sizes = size_div.find_next_sibling("select")
        selected_size = None

        for option in sizes.find_all("option"):
            if "selected" in option.attrs:
                selected_size = option.text.strip()
                break

        availability = "Na sklade" if "add-to-cart" in response.text else "Vypredané"
        return {
            "name": name,
            "image": image,
            "size": selected_size,
            "availability": availability
        }
    except Exception as e:
        return {"error": str(e), "url": url}

def main():
    results = []
    for url in urls:
        results.append(get_data(url))

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
