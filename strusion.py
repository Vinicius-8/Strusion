import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname("__file__"), '..'))
sys.path.append(path)
import argparse
import IO
from Strusion import subtitles


parser = argparse.ArgumentParser(description="Subtitle Merger")
parser.add_argument("-S", "--subtitles", nargs=2, help="Subtitles to fuse",
                    required=False)
parser.add_argument("-s", "--subtitle", nargs=1, help="Subtitle",
                    required=False)
parser.add_argument("-o", "--output", nargs=1, help="output file",
                    required=False)
parser.add_argument("-x", "--x_axis", nargs=1,
                    help="X axis pixels that stays above", required=False)

parser.add_argument("-y", "--y_axis", nargs=1,
                    help="Y axis pixels that stays above", required=False)

parser.add_argument("-c", "--color", nargs=1,
                    help="subtitle color", required=False)

parser.add_argument("-d", "--delay", nargs=2,
                    help="Increase or decrease the delay in a sub, put the "
                         "millisecs then sub",
                    required=False)


def main():
    args = parser.parse_args()
    if args.subtitles: 	 	# non empty args for 2 subs
        if is_srt(args.subtitles[0]) and is_srt(args.subtitles[1]):
            subtitle_merged = subtitles.merge_two_subtitles(
                args.subtitles[0],
                args.subtitles[1],
                color=args.color[0] if args.color else None,
                x_axis=args.x_axis[0] if args.x_axis else None,
                y_axis=args.y_axis[0] if args.y_axis else None)

            IO.output_file(args.output[0] if args.output  # put into a srt file
                           else config_default_output(args.subtitles[0]),
                           subtitle_merged)
        else:
            print('\n\n>> [Fail] For now, only srt files are supported')

    elif args.subtitle:	 # one sub
        if is_srt(args.subtitle[0]):
            subtitle = subtitles.change_one_subtitle(
                args.subtitle[0],
                color=args.color[0] if args.color else None,
                x_axis=args.x_axis[0] if args.x_axis else None,
                y_axis=args.y_axis[0] if args.y_axis else None)

            IO.output_file(args.output[0] if args.output
                           else config_default_output(args.subtitle[0]),
                           subtitle)
        else:
            print('\n\n>> [Fail] For now, only srt files are supported')

    elif args.delay:
        if is_srt(args.delay[1]):
            try:
                int(args.delay[0])
            except ValueError:
                print('\n\n>.[Fail] \'{}\' is not integer'
                      .format(args.delay[0]))
                return
            subtitle = subtitles.change_subtitle_delay(args.delay[0],
                                                       args.delay[1])
            IO.output_file(args.output[0] if args.output
                           else config_default_output(args.subtitle[0]),
                           subtitle)
        else:
            print('\n\n>> [Fail] For now, only srt files are supported')


# refatorar isso aqui pro caso de nomes com pontos
def config_default_output(path):  # adds .mod. to file name
    index = path.rfind('.')
    _path = str(path[:index] + ".mod." + path[index + 1:])
    print("\n>> Output: {}".format(_path))
    return _path


def is_srt(sub):
    frag = sub.split('.')          # refatorar essa aqui tbm
    return frag[-1] == 'srt'


if __name__ == '__main__':

    main()
    print('\n> done')
