# 
# Example file for retrieving data from the internet
#
import urllib.request


def main():
  webUrl = urllib.request.urlopen("http://www.google.com")
  print("response is ::: ", webUrl.getcode())

if __name__ == "__main__":
  main()
