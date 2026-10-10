from bs4 import BeautifulSoup

def run_bs4():
    html_doc = "<html><body><h1>Привіт, світ!</h1></body></html>"
    soup = BeautifulSoup(html_doc, 'html.parser')
    print("[BeautifulSoup] Знайдений текст заголовка:", soup.h1.text)
