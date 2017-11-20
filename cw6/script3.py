from urllib2 import urlopen

def saveHTMLPage(url, path, filename):
    with open('{}/{}.txt'.format(path,filename), 'w') as file:
        file.write(urlopen(url).read())


saveHTMLPage('http://www.hibernatespatial.org/documentation/documentation/', 'C:/Users/student/bs/repos/cw6', 'doc')