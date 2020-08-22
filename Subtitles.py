import IO
from argparse import ArgumentParser

#  Default values
x_axis = 192 			# x axis for second sub
y_axis = 48				# y axis for second sub
y_axis_bottom = 268		# y axis for second sub

default_sub_color = "ffffff"


def merge_two_subtitles(args):
    sub1 = IO.load(args.subtitles[0])  # loading file
    sub2 = IO.load(args.subtitles[1])  # ''

    sub_position_str = set_position(args)
    color_str = set_color(args)
    control = False  # control var to indicates that is a new sub block
    sub1.append('')

    for i in range(len(sub2)):

        if 'ï»¿' in sub2[i]:
            sub2[i] = sub2[i][len(sub2[i]) - 1]

        if control:  # goes into because is the firstline without -->
            sub1.append(sub_position_str + color_str + sub2[i])  # add the first line
            control = False

        elif sub2[i] != '':
            sub1.append(sub2[i])  # add the subsequent lines

        else:
            sub1.append("</font>")  # add the last line
            sub1.append("")

        if '-->' in sub2[i]:  # from here, the code goes to a new sub block
            control = True
    return sub1


def change_one_subtitle(args):
    sub1 = IO.load(args.subtitle[0])
    sub_out = list()

    sub_position_str = set_position(args)
    color_str = set_color(args)
    control = False
    sub1.append('')

    for i in range(len(sub1)):

        if 'ï»¿' in sub1[i]:
            sub1[i] = sub1[i][len(sub1[i]) - 1]

        if control:

            print('-> ', sub1[i])
            sub_out.append(sub_position_str + color_str + sub1[i])
            control = False

        elif sub1[i] != '':

            sub_out.append(sub1[i])  # add the subsequent lines

        else:
            sub_out.append("</font>")  # add the last line
            sub_out.append("")

        if '-->' in sub1[i]:  # from here, the code goes to a new sub block
            control = True

    return sub_out


def set_position(args):
    """
    Define the subtitle position on top
    :param args:
    :return:
    """

    # two different position exists for the y axis, that's why the extra 'if' in y,
    x = args.x_axis[0] if args.x_axis else x_axis  # se false usa o default
    y = args.y_axis[0] if args.y_axis else (y_axis_bottom if args.subtitle else y_axis)
    return "{\pos(" + str(x) + "," + str(y) + ")}"


def set_color(args):
    return "<font color=\"" + (args.color[0] if args.color else default_sub_color) + "\">"
