import argparse
from IO import IO

io = IO() # object for I/O

parser = argparse.ArgumentParser(description="Subtitle Fuser")


parser.add_argument("-S","--subtitles",nargs=2,help="Subtitles to fuse", required=False)
parser.add_argument("-s","--subtitle",nargs=1,help="Subtitle", required=False)
parser.add_argument("-o","--output",nargs=1,help="output file", required=False)
parser.add_argument("-x","--x_axis",nargs=1,help="X axis pixels that stays above", required=False)
parser.add_argument("-y","--y_axis",nargs=1,help="Y axis pixels that stays above", required=False)
parser.add_argument("-c","--color",nargs=1,help="subtitle color", required=False)


args = parser.parse_args()	

#Default values
x_axis = 192 			# x axis for second sub
y_axis = 48				# y axis for second sub
y_axis_bottom = 268		# y axis for second sub

sub_position_str = "{\pos(" + str(x_axis) + "," + str(y_axis) + ")}"
sub_color = "ffffff"

def main():
	
	if args.subtitles: # non empty args for 2 subs
		leg1 = io.load(args.subtitles[0])	#loading file
		leg2 = io.load(args.subtitles[1])	# ''
			

		sub_position_str = setPosition()	 	
		color_str = setColor()

		control = False #	control var to indicates that is a new sub block
		leg1.append('')									

		for i in range(len(leg2)):						

			if 'ï»¿' in leg2[i]:							
				leg2[i] = leg2[i][len(leg2[i])-1]	

			if control:													# goes into because is the firstline without -->
				leg1.append(sub_position_str+color_str+leg2[i])  		# add the first line
				control = False							

			elif leg2[i] != '':
				leg1.append(leg2[i])									# add the subsequent lines			

			else:			
				leg1.append("</font>")									# add the last line
				leg1.append("")
			
			if '-->' in leg2[i]:										# from here, the code goes to a new sub block
				control = True
				

		
		io.outputfile(args.output[0] if args.output else configDefaultOutput(args.subtitles[0]), leg1) 			#put into a srt file

	elif args.subtitle:		#one sub 								
		leg1 = io.load(args.subtitle[0])
		legOut = list()

		sub_position_str = setPosition()	 	
		color_str = setColor()
		
		control = False
		leg1.append('')									
		for i in range(len(leg1)):

			if 'ï»¿' in leg1[i]:							
				leg1[i] = leg1[i][len(leg1[i])-1]

			if control:
				legOut.append(sub_position_str+color_str+leg1[i])
				control = False

			elif leg1[i] != '':
				legOut.append(leg1[i])									# add the subsequent lines			

			else:			
				legOut.append("</font>")									#add the last line
				legOut.append("")
			
			if '-->' in leg1[i]:										# from here, the code goes to a new sub block
				control = True

		io.outputfile(args.output[0] if args.output else configDefaultOutput(args.subtitle[0]), legOut)


def setPosition():	
	''' 
	two different position exists for the y axis, that's why the extra 'if' in y,
	'''
	x = args.x_axis[0] if args.x_axis else x_axis
	y =	args.y_axis[0] if args.y_axis else (y_axis_bottom if args.subtitle else y_axis)

	return "{\pos(" + str(x) + "," + str(y) + ")}"

def setColor():
	return "<font color=\""+(args.color[0] if args.color else sub_color)+"\">"

def configDefaultOutput(path):
	index = path.rfind('.')
	_path = str(path[:index]+".mod."+path[index+1:])
	print("\n>> Output: {}".format(_path))
	return _path

main()



