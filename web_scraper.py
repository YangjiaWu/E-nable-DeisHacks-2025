from bs4 import BeautifulSoup as bs
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1'
}

url = "https://3d.nih.gov/entries/3DPX-020291"
response = requests.get(url, headers=headers)

# print(response)
if response.status_code == 200:

    # Print the first 500 characters of the HTML response for inspection
    print(response.text)

    
    # Parse the HTML content with BeautifulSoup
    soup = bs(response.text, 'lxml')

    # Find all <p> tags
    p_tags = soup.find_all('p')
    
    # Print all <p> tags
    for p in p_tags:
        print(p.prettify())  # prettify() formats the tag nicely

    # # Convert BeautifulSoup object to an lxml Element
    # html_tree = etree.HTML(str(soup))

    # # XPath query to extract the number (assuming it's the text in the <p> tag)
    # number = html_tree.xpath('//*[@id="app"]/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/ul[2]/li[1]/p')
    # print(number)  # Expected output: "253"


    # soup = bs(response.text, 'html.parser')
    # p_tags = soup.select('p.mb-0')
    # print(p_tags)

    # p_tag = soup.find_all('p', class_='mb-0')

    # print(p_tag)

    # for tag in p_tag:
    #     print(tag)
    #     for child in tag.children:
    #         print(child)

    # for child in p_tag.find_all():
    #     child.decompose()

    # number = p_tag.text.strip()
    # print(number)
else:
    print('got error response')
    print(response)

