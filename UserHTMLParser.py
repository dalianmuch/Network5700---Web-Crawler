from HTMLParser import HTMLParser

class UserHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.pages = []

    def handle_starttag(self, tag, attrs):
        if tag == "a" and len(attrs) == 1:
            if attrs[0][0] == "href" and attrs[0][1].find("fakebook") != -1:
                self.pages.append(attrs[0][1])
