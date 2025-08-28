# Goodreads Quotes Scraper 📝🤖
 ____  _____ _____ _       ____  ____ _____ 
/  __\/  __//    // \     /  __\/  _ Y__ __\
|  \/||  \  |  __\| |     | | //| / \| / \  
|    /|  /_ | |   | |     | |_\\| \_/| | |  
\_/\_\\____\\_/   \_/_____\____/\____/ \_/  
                     \____\       R   E   P   B   O   T

> **Scraping project by [Refi Tri Hidayatullah](https://github.com/refitrihidayatullah) — `repbot`**

---
## 📖 download here!
👉 [**Download Goodreads Scraper (Windows .exe)**](https://github.com/refitrihidayatullah/web_scraping_quotes/releases/download/v1.0/scraper.exe)

## 📖 Deskripsi

Proyek ini adalah <strong>web scraping tool</strong> untuk mengambil kutipan (quotes) dari 
<a href="https://www.goodreads.com/quotes" target="_blank">Goodreads Quotes</a>. 
Data yang dikumpulkan meliputi:

- **No** → nomor urut quote  
- **Quote** → teks kutipan  
- **Author** → penulis quote  
- **Tags** → kategori atau label quote  

Semua data akan otomatis disimpan dalam file **Excel (`.xlsx`)** dengan nama:  
yang akan tersimpan langsung di **Desktop** pengguna.

---

## 🛠️ Teknologi

- [Python 3](https://www.python.org/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas](https://pandas.pydata.org/)
- [tqdm](https://tqdm.github.io/) (progress bar)
- [openpyxl](https://openpyxl.readthedocs.io/) (engine Excel)

---

## 🚀 Cara Install & Jalankan

1. **Clone repository**
   ```bash
   git clone git@github.com:refitrihidayatullah/web_scraping_quotes.git
   cd web_scraping_quotes
2. **Buat virtual environment** 
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
3. **Install dependencies** 
    pip install  .. isi sesuai yang diperlukan misal
    pip install Requests dsb
4. **Jalankan program**
    python scraper.py

📦 Build ke .exe

Jika ingin membuat versi portable .exe:

1. **Install pyinstaller**
   pip install pyinstaller
2. **Build executable**
   pyinstaller --onefile scraper.py
3. **Hasil .exe akan ada di folder:**
   dist/scraper.exe

💾 Download .exe

Jika tidak ingin repot build, kamu bisa langsung download file .exe di sini:

👉 [**Download Goodreads Scraper (Windows .exe)**](https://github.com/refitrihidayatullah/web_scraping_quotes/releases/download/v1.0/scraper.exe)



✨ Output Contoh

File Excel hasil scraping (goodreads_quotes_by_repbot.xlsx) akan berisi:

| No | Quote                               | Author       | Tags                |
| -- | ----------------------------------- | ------------ | ------------------- |
| 1  | Be yourself; everyone else is taken | Oscar Wilde  | inspirational, life |
| 2  | In three words I can sum up...      | Robert Frost | life                |

👨‍💻 Author

Refi Tri Hidayatullah

🤖 Create Scraping Web by Refi Tri Hidayatullah — repbot

⚠️ Disclaimer

Scraping ini hanya untuk kepentingan belajar.
Gunakan secara bijak dan jangan overload server target