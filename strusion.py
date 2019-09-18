import argparse
from IO import IO

io = IO() # object for I/O

parser = argparse.ArgumentParser(description="Subtitle Fuser")

parser.add_argument("-S","--subtitles",nargs=2,help="Subtitles to fuse", required=False)
parser.add_argument("-s","--subtitle",nargs=1,help="Subtitle", required=False)
parser.add_argument("-o","--output",nargs=1,help="output file", required=True)
parser.add_argument("-x","--x_axis",nargs=1,help="X axis pixels that stays above", required=False)
parser.add_argument("-y","--y_axis",nargs=1,help="Y axis pixels that stays above", required=False)

args = parser.parse_args()	

if args.subtitles: # non empty args
	leg1 = io.load(args.subtitles[0])	#loading file
	leg2 = io.load(args.subtitles[1])	# ''
	
	x_axis = 200 	# x axis for second sub
	y_axis = 45		# y axis for second sub

	if args.x_axis:				
		x_axis = args.x_axis[0]
	if args.y_axis:
		y_axis = args.y_axis[0]		

	position = "{\pos(" + str(x_axis) + "," + str(y_axis) + ")}" # Monta a string de posição para adionar na legenda	

	control = False #	control var
	leg1.append('')									# adds a empty line
	for i in range(len(leg2)):						# running througth every second line sub

		if 'ï»¿' in leg2[i]:						# special character verification	
				leg2[i] = leg2[i][len(leg2[i])-1]	# removing it
		
		if control:
			leg1.append(position+leg2[i])			# adding the second sub line to the end of first sub + position x and y
			control = False							
		else:			
			leg1.append(leg2[i])					# adding without position
		

		if '-->' in leg2[i]:						# cheking if the line needs position params 
			control = True

	io.outputfile(args.output[0], leg1) 			#put into a srt file
elif args.subtitle:
	print('Unica sub')
else:
	print("Argumentos insuficientes")
	exit()