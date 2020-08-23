
def load(path):  # abre o aquivo e transforma em lista
    obj_txt = ''
    re = ''
    try:
        obj_txt = open(path, encoding="utf8") # por padrão é aberto em r
        re = list(obj_txt.read().splitlines())

    except UnicodeDecodeError:
        obj_txt = open(path, encoding="ISO-8859-1")
        re = list(obj_txt.read().splitlines())

    except FileNotFoundError:

        print("The file was not found")
        exit()      # sai do script

    obj_txt.close()
    for ele in range(0, len(re)):
        re[ele] = re[ele].strip() # eliminando quarquer tipo de espaço em cada linha
    return re


def output_file(outputpath, lista): # joga os dados em um txt
    o = open(outputpath, 'a+', encoding="utf8")

    for a in lista:
        o.write(f"{a}\n")
    o.close()
