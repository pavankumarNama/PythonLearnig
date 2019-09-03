# demonstrate template string functions
from string import Template


def main():
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # TODO: create a template with placeholders
    temp = Template("Author Name : ${authorName} and Language is : ${language}")
    # TODO: use the substitute method with keyword arguments
    str1 = temp.substitute(authorName="Joe Marini", language="Python")
    # TODO: use the substitute method with a dictionary
    d = {"authorName" : "Joe Marini", "language" : "Python"}
    str2 = temp.substitute(d)
    print(str1)
    print(str2)


if __name__ == "__main__":
    main()
