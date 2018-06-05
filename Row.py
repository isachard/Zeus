import csv


class Row(object):

    def __init__(self, thrends):
        with open('oddThreads.csv', 'wb') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_ALL)

            for list in thrends:
                filewriter.
