import requests

from bs4 import BeautifulSoup as bs


if __name__ == '__main__':

    # load the projectpro webpage content

    r = requests.get('https://www.google.com/search?q=sheep%20pictures&tbm=isch&tbs=isz:m&hl=zh-CN&sa=X&ved'
                     '=0CAMQpwVqFwoTCPDD4_CCjvkCFQAAAAAdAAAAABAE&biw=1440&bih=821')

    # convert to beautiful soup

    soup = bs(r.content)

    print(soup.prettify())
