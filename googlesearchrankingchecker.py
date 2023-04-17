import requests    
from bs4 import BeautifulSoup

def get_google_results(query):
    res = requests.get(f'https://www.google.com/search?q={query}') 
    soup = BeautifulSoup(res.text, 'html.parser')
    results = []
    for i, link in enumerate(soup.find_all('a')):
        href = link.get('href')
        if href.startswith('/url?q='):
            href = href.split('/url?q=')[1].split('&')[0]
            results.append(href)
    return results

def get_ranking(keyword, url):
    results = get_google_results(keyword)
    for i, result in enumerate(results):
        if url in result:
            return i + 1
    return -1

# Example usage
keyword = 'home decor ideas' # Type your keyword here inside the single inverted commas
url = 'https://www.housebeautiful.com/home-remodeling/diy-projects/g1242/quick-easy-home-decorating-ideas-0612/'  # add your url here in these single inverted commas 
ranking = get_ranking(keyword, url)
if ranking == -1:
    print(f'The website {url} does not rank for the keyword "{keyword}"')
else:
    print(f'The website {url} ranks #{ranking} for the keyword "{keyword}"')































