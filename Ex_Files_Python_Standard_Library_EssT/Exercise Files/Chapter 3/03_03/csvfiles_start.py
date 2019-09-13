# Reading and writing Comma Separate Values files with Python
import csv


# TODO: list the dialects that are available to use
# print(csv.list_dialects())

# TODO: Open a CSV file and read each row of data
def readerSample():
    with open('StockQuotes.csv', 'r') as data:
        reader = csv.reader(data)
        for row in reader:
            print(row)


# TODO: Use the CSV module Sniffer to see what dialect of CSV this is
def useSniffer():
    with open('StockQuotes.csv', 'r') as data:
        dialect = csv.Sniffer().sniff(data.read(1024))
        data.seek(0)
        has_header = csv.Sniffer().has_header(data.read(1024))
        print("Has Headers: ", has_header)
        print(dialect.delimiter)
        print(dialect.doublequote)
        print(dialect.escapechar)
        print(dialect.quotechar)
        print(dialect)

# TODO: Write data to a CSV file
def writerSample():
    with open('SampleCSV.csv', 'w') as cfp:
        csvwritter = csv.writer(cfp)
        csvwritter.writerow(['Pavan', 'Kumar', '23'])
        csvwritter.writerow(['Ravi', 'Kumar', '20'])
        csvwritter.writerow(['Krishna', 'Kumar', '25'])


# Exercise the samples
# readerSample()
writerSample()
# useSniffer()
