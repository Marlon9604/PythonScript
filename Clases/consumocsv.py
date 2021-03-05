import random
import csv

class LecturaCSV():
    def leer(self, start: int, stop: int):
        with open('clases/lista.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            num = random.randrange(start,stop)
            retorno = ""
            for row in csv_reader:
                if line_count == num:
                    retorno = row
                    line_count += 1
                    break
                else:
                    line_count += 1
        
        return retorno

