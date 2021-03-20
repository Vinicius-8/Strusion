import IO
from math import floor
from tqdm import tqdm
#  Default values
x_axis = 192 			# x axis for second sub
y_axis = 48				# y axis for second sub
y_axis_bottom = 268		# y axis for second sub

default_sub_color = "ffffff"


def merge_two_subtitles(path_sub_1, path_sub_2, color=None,
                        x_axis=None, y_axis=None):
    sub1 = IO.load(path_sub_1)  # loading file
    sub2 = IO.load(path_sub_2)  # ''

    sub_position_str = set_position(
        axis_x=x_axis, axis_y=y_axis, one_subtitle=False)
    color_str = set_color(color)
    control = False  # control var to indicates that is a new sub block
    sub1.append('')

    for i in tqdm(range(len(sub2))):
        if 'ï»¿' in sub2[i]:
            sub2[i] = sub2[i][len(sub2[i]) - 1]

        if control:  # goes into because is the firstline without '-->'
            # add the first line
            sub1.append(sub_position_str + color_str + sub2[i])
            control = False

        elif sub2[i] != '':
            sub1.append(sub2[i])  # add the subsequent lines

        else:
            sub1.append("</font>")  # add the last line
            sub1.append("")

        if '-->' in sub2[i]:  # from here, the code goes to a new sub block
            control = True
    return sub1


def change_one_subtitle(path_sub, color=None, x_axis=None, y_axis=None):
    sub1 = IO.load(path_sub)
    sub_out = list()

    sub_position_str = set_position(
        axis_x=x_axis,
        axis_y=y_axis,
        one_subtitle=True)
    color_str = set_color(color)
    control = False
    sub1.append('')
    for i in tqdm(range(len(sub1))):
        if 'ï»¿' in sub1[i]:
            sub1[i] = sub1[i][len(sub1[i]) - 1]

        if control:
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


def change_subtitle_delay(millis, path_sub):
    millisecs = int(millis)
    sub = IO.load(path_sub)
    for i in tqdm(range(len(sub))):
        if '-->' in sub[i]:
            slices = sub[i].split(" --> ")
            ini = format_string_to_millisecs(slices[0])
            end = format_string_to_millisecs(slices[1])
            modification = "{} --> {}".format(
                format_millisecs_to_string(ini + millisecs),
                format_millisecs_to_string(end + millisecs))
            sub[i] = modification
    return sub


def set_position(one_subtitle, axis_x=None, axis_y=None):  # axis
    """
    Define the subtitle position on top
    :param axis_x, axis_y:
    :return:
    """

    # two different position exists for the y axis,
    # that's why the extra 'if' in y,
    x = axis_x if axis_x else x_axis  # se false usa o default
    y = axis_y if axis_y else (y_axis_bottom if one_subtitle else y_axis)
    return "{\\pos(" + str(x) + "," + str(y) + ")}"


def set_color(color):
    return "<font color=\"" + (color if color else default_sub_color) + "\">"


def format_millisecs_to_string(millis):
    millis = str(millis)
    millisecs = int(millis[-3:])
    millis = int(millis)
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24
    string_formated = "{:02d}:{:02d}:{:02d},{:03d}"\
        .format(floor(hours), minutes, seconds, millisecs)
    return string_formated


def format_string_to_millisecs(string):
    # all the vars are in millisecs
    slices = string.split(':')
    hour = int(slices[0]) * (1000 * 60 * 60)
    minutes = int(slices[1]) * (1000 * 60)
    slices2 = slices[2].split(',')
    seconds = int(slices2[0]) * 1000
    millisecs = int(slices2[1])
    total = hour + minutes + seconds + millisecs
    return total
