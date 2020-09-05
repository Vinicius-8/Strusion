import argparse
import IO
import Subtitles


parser = argparse.ArgumentParser(description="Subtitle Merger")
parser.add_argument("-S", "--subtitles", nargs=2, help="Subtitles to fuse", required=False)
parser.add_argument("-s", "--subtitle", nargs=1, help="Subtitle", required=False)
parser.add_argument("-o", "--output", nargs=1, help="output file", required=False)
parser.add_argument("-x", "--x_axis", nargs=1, help="X axis pixels that stays above", required=False)
parser.add_argument("-y", "--y_axis", nargs=1, help="Y axis pixels that stays above", required=False)
parser.add_argument("-c", "--color", nargs=1, help="subtitle color", required=False)
parser.add_argument("-d", "--delay", nargs=2, help="Increase or decrease the delay in a sub, put the millisecs then sub", required=False)
args = parser.parse_args()	


def main():
    if args.subtitles: 	 	# non empty args for 2 subs
        if isSrt(args.subtitles[0]) and isSrt(args.subtitles[1]):                    	
        	subtitle_merged = Subtitles.merge_two_subtitles(args)
        	IO.output_file(args.output[0] if args.output else config_default_output(args.subtitles[0]), subtitle_merged) 			#put into a srt file
        else:
    	    print('\n\n>> [Fail] For now, only srt files are supported')
                       
    elif args.subtitle:		# one sub        
        if isSrt(args.subtitle[0]):
        	subtitle = Subtitles.change_one_subtitle(args)
        	IO.output_file(args.output[0] if args.output else config_default_output(args.subtitle[0]), subtitle)               
        else:
        	print('\n\n>> [Fail] For now, only srt files are supported')
        

    elif args.delay:
    	if isSrt(args.delay[1]):   
            try:
                int(args.delay[0])
            except ValueError:
                print('\n\n>.[Fail] \'{}\' is not integer'.format(args.delay[0]))
                return
            subtitle = Subtitles.change_subtitle_delay(args)
            IO.output_file(args.output[0] if args.output else config_default_output(args.subtitle[0]), subtitle)    
    	else:
    		print('\n\n>> [Fail] For now, only srt files are supported')

        

def config_default_output(path):
    index = path.rfind('.')
    _path = str(path[:index]+".mod."+path[index+1:])
    print("\n>> Output: {}".format(_path))
    return _path

def isSrt(sub):
	frag = sub.split('.')
	return frag[-1] == 'srt'


main()
print('\n> done')



