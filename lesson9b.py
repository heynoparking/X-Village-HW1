from requests_html import HTMLSession

session = HTMLSession()
response = session.get('http://quotes.toscrape.com/')
link_set = set()
elements = response.html.find('.quote span a')
for element in elements:
    link_set.add(element.attrs['href'])
print(link_set)