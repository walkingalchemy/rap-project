from lxml import html
import requests

page = requests.get('http://rapgenius.com/Sage-francis-andy-kaufman-lyrics')
tree = html.fromstring(page.text)

lyric1 = tree.xpath('//*[@id="main"]/div[1]/div[2]/div[8]/p')
lyric2 = tree.xpath('//*[@id="main"]/div[1]/div[2]/div[8]/p/a[1]')
lyric3 = tree.xpath('//*[@id="main"]/div[1]/div[2]/div[8]/p/a[2]')
lyric4 = tree.xpath('//*[@id="main"]/div[1]/div[2]/div[8]/p/text()[2]')

print lyric1[0].text
print lyric2[0].text
print lyric3[0].text
print lyric4[0].text

store = open('testpage', 'w')
store.write(html.tostring(tree))
store.close()
print "Fin"
