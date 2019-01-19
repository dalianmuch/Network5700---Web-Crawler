from HTMLParser import HTMLParser

class SecretFlagHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.has_flag = False
        self.secret_flag = ""

    def handle_starttag(self, tag, attrs):
        if tag == "h2" and len(attrs) == 2:
            if attrs[0][0] == "class" and attrs[0][1] == "secret_flag":
                if attrs[1][0] == "style" and attrs[1][1] == "color:red":
                    self.has_flag = True

    def handle_endtag(self, tag):
        if tag == "h2" and self.has_flag == True:
            self.has_flag = False

    def handle_data(self, data):
        if self.has_flag == True and data.find("FLAG: ") == 0:
            self.secret_flag = data[6:]
