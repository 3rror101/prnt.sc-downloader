from bs4 import BeautifulSoup as bs
import urllib.request

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
data = open("count", "r")
lines = data.readlines()
linka = lines[0][:-1]
linkb = lines[1]
data.close()

print(linka)
print(linkb)

def getphoto(link):
    print(link)
    request = urllib.request.Request('https://prnt.sc/' + link, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    html_doc = response.read()
    soup = bs(html_doc, 'html.parser')
    strhtm = soup.prettify()
    photo = strhtm[1800:].split('"')[0]
    if photo[0] == '/':
        photo = 'https:' + photo
    print(photo)
    try:
        extenstion = photo.split('.')[-1]
        urllib.request.urlretrieve(photo, f'Photos/{link}.{extenstion}')
    except:
        f = open('Photos/'+link,'w+')
        f.write(photo)
        f.close

def main():
    global linka
    global linkb
    getphoto(linka+linkb)
    while True:
        linkb = int(linkb)
        linkb += 1
        linkb = str(linkb)
        if linkb == '10000':
            linkb = '0000'
            if linka[1] == 'z':
                if linka == 'zz':
                    break
                linka = alph[alph.index(linka[0]) + 1] + alph[0]
            else:
                linka = linka[0] + alph[alph.index(linka[1])+1]
                
        while len(linkb) < 4:
            linkb = '0' + linkb
        getphoto(linka+linkb)
        data = open("count", "w")
        data.write(linka + '\n' + linkb)

main()
