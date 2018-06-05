
class Parser:

    def parseTable(self, table):
        trends = []
        i = 0
        for row in table:

            lista = row.text.split()[:]
            #print(lista)
            if len(lista) == 17:
                trends.append(lista)
        print(trends)
        return trends
        