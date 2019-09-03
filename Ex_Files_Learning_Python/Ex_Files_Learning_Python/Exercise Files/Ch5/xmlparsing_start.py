# 
# Example file for parsing and processing XML
#
import xml.dom.minidom

def main():
  # use the parse() function to load and parse an XML file
  xmlParse = xml.dom.minidom.parse("samplexml.xml")

  # print out the document node and the name of the first child tag
  print(xmlParse.nodeName)
  print(xmlParse.firstChild.tagName)
  
  # get a list of XML tags from the document and print each one
  skills = xmlParse.getElementsByTagName("skill")
  print(skills.length)
  for skill in skills:
    print(skill.getAttribute("name"))
    
  # create a new XML tag and add it into the document
  newEle = xmlParse.createElement("skill")
  newEle.setAttribute("name", "Java")
  xmlParse.firstChild.appendChild(newEle)

  skills = xmlParse.getElementsByTagName("skill")
  print(skills.length)
  for skill in skills:
    print(skill.getAttribute("name"))

if __name__ == "__main__":
  main();

