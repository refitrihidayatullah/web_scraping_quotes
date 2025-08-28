import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from tqdm import tqdm

def show_banner():
    banner = r"""
 ____  _____ _____ _       ____  ____ _____ 
/  __\/  __//    // \     /  __\/  _ Y__ __\
|  \/||  \  |  __\| |     | | //| / \| / \  
|    /|  /_ | |   | |     | |_\\| \_/| | |  
\_/\_\\____\\_/   \_/_____\____/\____/ \_/  
                     \____\       R   E   P   B   O   T
    """
    print(banner)
    print("target url : https://www.goodreads.com/quotes")
    print("\n🤖 Create Scraping Web by Refi Tri Hidayatullah -- repbot\n")

def main():
    base_url = "https://www.goodreads.com/quotes?page={}"
    headers = {"User-Agent": "Mozilla/5.0"}

    data = []
    max_pages = 100  # misalnya batas maksimal 100 halaman

    for page in tqdm(range(1, max_pages+1), desc="Scraping"):
        response = requests.get(base_url.format(page), headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        quote_blocks = soup.find_all("div", class_="quote")
        if not quote_blocks:
            break

        for i, block in enumerate(quote_blocks, start=len(data) + 1):
            text = block.find("div", class_="quoteText").get_text(strip=True).split("―")[0]
            author = block.find("span", class_="authorOrTitle")
            author = author.get_text(strip=True) if author else "Unknown"
            tags = block.find("div", class_="greyText smallText left")
            tags = tags.get_text(strip=True).replace("tags:", "") if tags else ""

            data.append({"No": i, "Quote": text, "Author": author, "Tags": tags})

        time.sleep(1)

    df = pd.DataFrame(data)

    # simpan ke Desktop, fallback ke folder saat ini jika Desktop tidak ada
    desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
    if not os.path.exists(desktop):
        desktop = os.getcwd()
    output_path = os.path.join(desktop, "goodreads_quotes_by_repbot.xlsx")
    df.to_excel(output_path, index=False)
    print(f"✅ created {output_path}")

if __name__ == "__main__":
    show_banner()
    main()
    input("\n✅ Selesai! Tekan ENTER untuk keluar... <=== REP_BOT")
