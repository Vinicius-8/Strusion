import argparse
from IO import IO

io = IO() # objeto de entrada e saída de dados

parser = argparse.ArgumentParser(description="Fusor de Legendas")

parser.add_argument("-l","--legendas",nargs=2,help="Legendas para a fusao", required=True)
parser.add_argument("-o","--output",nargs=1,help="Nome do arquivo a ser gerado", required=True)
parser.add_argument("-x","--x_axis",nargs=1,help="Quantidade de pixes de distancia no eixo de X", required=False)
parser.add_argument("-y","--y_axis",nargs=1,help="Quantidade de pixes de distancia no eixo de Y", required=False)

args = parser.parse_args()	# Atribuindo os argumentos a uma variável

if args.legendas: #verficando se os argumentos estão presentes
	leg1 = io.load(args.legendas[0])	#carregando o arquivo
	leg2 = io.load(args.legendas[1])	# ''
	
	x_axis = 200 	# posição padrão do eixo de x
	y_axis = 45		# posição padrão do eixo de y

	if args.x_axis:				# Verifica se o parametro foi definido para adicionalo
		x_axis = args.x_axis[0]
	if args.y_axis:
		y_axis = args.y_axis[0]		

	position = "{\pos(" + str(x_axis) + "," + str(y_axis) + ")}" # Monta a string de posição para adionar na legenda	

	control = False #	Variavel de controle

	leg1.append('')									# Adicionando uma linha vazia
	for i in range(len(leg2)):						# Percorrendo todas as linhas da segunda legenda

		if 'ï»¿1' in leg2[i]:						# Verificando a existência de um caractere especial	
				leg2[i] = leg2[i][len(leg2[i])-1]	# Removendo o caractere especial
		
		if control:
			leg1.append(position+leg2[i])			# acidionando o a linha atual da legenda 2 no final da legenda 1 + posição
			control = False
		else:			
			leg1.append(leg2[i])					# adicionando sem posição
		

		if '-->' in leg2[i]:						# Verifica se é a linha correta para inserir a posição
			control = True

	io.outputfile(args.output[0], leg1) 			# Gravando a legenda 1 (com o acréscimo da legenda 2) em um arq srt

else:
	print("Argumentos insuficientes")
	exit()