from urllib.request import urlopen
from bs4 import BeautifulSoup
import json, re, ezgmail, os
import psycopg2

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
ezgmail.init()

hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'test_db_news'

conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

def our_query(conn):
    cur = conn.cursor()
    cur.execute("""select * from news""")
    rows = cur.fetchall()

    for row in rows :
        print (row[1])

# our_query(conn)
# conn.close()


def mydata(conn):
    html = urlopen('https://inshorts.com/en/read')

    soup = BeautifulSoup(html, 'html.parser')

    postings = soup.find_all("div", class_="news-card")

    cur = conn.cursor()

    for p in postings:
        url = 'https://inshorts.com' + p.find('a', class_='clickable')['href']
        title = p.find(attrs={"itemprop": "headline"}).text.replace("'", r"")
        author = p.find('span', class_='author').text.replace("'", r"")
        description = p.find(attrs={"itemprop": "articleBody"}).text.replace("'", r"")
        try:
            cur.execute("""insert into news ("url", "title", "author", "description") values ('{}','{}','{}','{}')""".format(url,title,author,description))
            print('%s added' % (title,))
        except:
            print('%s already exist' % (title,))
    
    conn.commit()

    ezgmail.send('guptaa.ankitt@gmail.com', 'trial email from python', title)

    # self.stdout.write( 'job complete' )

    # context = ({"url" : url, "title" : title, "author" : author, "description" : description})

    # html = '<p> <a href="{{url}}"><h1>{{title}}</h1></a> <h2>{{author}}</h2> <br> {{description}} </p>'
    # html_content = render_to_string(html, context)

mydata(conn)
conn.close()