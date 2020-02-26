# pip install bs4, requests
import requests, sys, webbrowser, bs4, time

print('Searching......')
res = requests.get('https://www.amazon.com/s?k=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('a.a-link-normal.a-text-normal')[0::2]

num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://www.amazon.com' + link_elems[i].get('href')
    print('Opening ', url_to_open)
    webbrowser.open(url_to_open)
    time.sleep(0.1)