import xml.etree.ElementTree as ET

mytree = ET.parse('sample.xml')
root = mytree.getroot()

ns = {
    'content': 'http://purl.org/rss/1.0/modules/content/'
}

for x in root.findall('channel/item'):
    title =x.find('title').text
    content = x.find('content:encoded', ns).text
    print(title, content)