import urllib2
from xml.etree import ElementTree


def parse_xml(url):
    counts = []
    page = urllib2.urlopen(url)
    tree = ElementTree.parse(page)

    comments = tree.findall('comments/comment')

    for comment in comments:
        counts.append(int(comment.find('count').text))

    return sum(counts)

print parse_xml('http://python-data.dr-chuck.net/comments_42.xml')
print parse_xml('http://python-data.dr-chuck.net/comments_190012.xml')
