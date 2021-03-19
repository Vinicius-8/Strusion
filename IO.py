
def load(path):  # abre o aquivo e transforma em lista
    obj_txt = ''
    readed_obj = ''
    try:
        obj_txt = open(path, encoding="utf8") # por padrão é aberto em r
        readed_obj = list(obj_txt.read().splitlines())

    except UnicodeDecodeError:
        obj_txt = open(path, encoding="ISO-8859-1")
        readed_obj = list(obj_txt.read().splitlines())

    except FileNotFoundError:

        print("The file was not found")
        exit()      # sai do script

    obj_txt.close()
    for line in range(0, len(readed_obj)):
        readed_obj[line] = readed_obj[line].strip()  # eliminando qualrquer tipo de espaço em cada linha
    return readed_obj


def output_file(outputpath, lista): # joga os dados em um txt
    o = open(outputpath, 'a+', encoding="utf8")

    for a in lista:
        o.write(f"{a}\n")
    o.close()
