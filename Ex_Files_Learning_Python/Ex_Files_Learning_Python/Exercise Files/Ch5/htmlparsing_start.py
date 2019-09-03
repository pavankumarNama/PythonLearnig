# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

metacount = 0

class MyHtmlParser(HTMLParser):
  def handle_comment(self, data):
    print("comment encountered ", data)
    pos = self.getpos()
    print("line number %d and position" % pos[0], pos[1])

  def handle_data(self, data):
    if data.isspace():
      return

    print("data encountered ", data)
    pos = self.getpos()
    print("line number %d and position" % pos[0], pos[1])

  def handle_endtag(self, tag):
    print("end tag encountered ", tag)
    pos = self.getpos()
    print("line number %d and position" % pos[0], pos[1])

  def handle_starttag(self, tag, attrs):
    global metacount

    if tag == 'meta':
      metacount += 1

    print("start tag encountered ", tag)
    pos = self.getpos()
    print("line number %d and position" % pos[0], pos[1])

    if attrs.__len__() > 0:
      print('Attributes')
      for attr in attrs:
        print(attr[0], '=', attr[1])



def main():
  # instantiate the parser and feed it some HTML
  parser = MyHtmlParser()
  f = open("samplehtml.html")
  if(f.mode == 'r'):
    data = f.read()
    parser.feed(data)

if __name__ == "__main__":
  main();
  print("Meta Count :: ", metacount)
  