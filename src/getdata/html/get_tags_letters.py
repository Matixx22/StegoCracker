from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re
import binascii
from textwrap import wrap


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.start_tags = []
        self.end_tags = []

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag:", tag)
        self.tags.append(tag)
        self.start_tags.append(tag)

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        self.tags.append(tag)
        self.end_tags.append(tag)

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        pass


def get_data(filename):
    """
    Get all tags from HTML document

    Args:
        filename (str): HTML file path

    Raises:
        TODO jak coś będzie

    """

    # Code goes here...
    parser = MyHTMLParser()

    data = b''

    with open(filename, 'r') as file:
        # soup = BeautifulSoup(file.read(), 'xml')
        html = file.read()
        # parser.feed(file.read())
    tags = re.findall(r'<[^>]+>', html)

    for tag in tags:
        t = re.sub(r'(<\w+)[^>]*(>)', r'\1\2', tag)
        t = re.sub('[/<>1-9]', '', t)
        for char in t:
            bit = b'0' if char.islower() else b'1'
            data += bit
    #
    # for tag in soup.find_all():
    #     print(tag)

    # data = (parser.tags, parser.start_tags, parser.end_tags)
    # print(data)

    # data = wrap(data.decode(), 8)
    # print(data)

    # for chunk in data:
    #     print(text_from_bits(chunk), end='')

    # print(text_from_bits('1101000'))
    # //print(binascii.unhexlify('%x' % bin_data))

    return data






