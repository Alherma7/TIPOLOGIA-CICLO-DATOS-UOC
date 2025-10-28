#preprocessing

def extract_country(list_of_urls):
    urls = {}
    for url in list_of_urls:
        parts = url.strip("/").split("/")
        country = parts[-1]
        name = country.replace("-", " ").capitalize()
        urls[name] = url
    return urls

def clean_autor(texto):
    if texto == "NA":
        return "NA"
    return " ".join(texto.strip().split()[0:4])

