class IO:

    def __init__(self):
        pass

    def load(self, path): #abre o aquivo e transforma em lista
        try:
            objTxt = open(path, encoding="utf8") # por padrão é aberto em r
            re = list(objTxt.read().splitlines())
        
        except UnicodeDecodeError:
            objTxt = open(path, encoding="ISO-8859-1")
            re = list(objTxt.read().splitlines())

        except FileNotFoundError:

            print("O Aquivo não foi encontrado")
            exit()      #sai do script
        
        
        objTxt.close()
        for ele in range(0, len(re)):
            re[ele] = re[ele].strip() # eliminando quarquer tipo de espaço em cada linha
        return re

    def outputfile(self, outputpath, lista): # joga os dados em um txt
        o = open(outputpath, 'a+', encoding="utf8")
        
        for a in lista:
            o.write(f"{a}\n")
        o.close()