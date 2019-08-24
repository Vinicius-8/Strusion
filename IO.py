class IO:

    def __init__(self):
        pass

    def load(self, path): #abre o aquivo e transforma em lista
        try:
            objTxt = open(path) # por padrão é aberto em r
        except FileNotFoundError:
            print("O Aquivo não foi encontrado")
            exit()      #sai do script
        re = list(objTxt.read().splitlines())
        objTxt.close()
        for ele in range(0, len(re)):
            re[ele] = re[ele].strip() # eliminando quarquer tipo de espaço em cada linha
        return re

    def outputfile(self, outputpath, lista): # joga os dados em um txt
        o = open(outputpath, 'a+')
        for a in lista:
            o.write(f"{a}\n")
        o.close()