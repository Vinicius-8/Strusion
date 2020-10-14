import pytest

#importing from parent folder
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import subtitles

PATH = sys.path[0]

def test_merge_two_subtitles():
	sub1 = PATH+'/tests/subs/Matrix.eng.srt'
	sub2 = PATH+'/tests/subs/Matrix.por.srt'
	new_sub = subtitles.merge_two_subtitles(sub1, sub2)
	assert '<i>TRINITY: Is everything in place?' in new_sub
	assert '{\\pos(192,48)}<font color="ffffff"><i>- Está tudo pronto?' in new_sub
	
	with pytest.raises(ValueError):
		subtitles.merge_two_subtitles(-1, 0)
	
	with pytest.raises(SystemExit):	
		subtitles.merge_two_subtitles('sub1', 'sub2')


def test_change_one_subtitle_color():
	sub = PATH+'/tests/subs/Matrix.eng.srt'
	color = 'fafcfd'
	new_sub = subtitles.change_one_subtitle(sub, color=color)
	
	assert color in new_sub[2]
	assert color not in  new_sub[0] 
	assert color not in new_sub[1] 
	
	with pytest.raises(SystemExit):
		subtitles.change_one_subtitle('', color=color)

	with pytest.raises(TypeError):
		subtitles.change_one_subtitle(sub, color=-1)


def test_change_one_subtitle_axis():
	sub = PATH+'/tests/subs/Matrix.eng.srt'
	x_axis = 200 			
	y_axis = 60
	new_sub = subtitles.change_one_subtitle(sub, x_axis=x_axis, y_axis=y_axis)

	assert '({},{})'.format(x_axis, y_axis) in new_sub[2]
	assert '(192, 48)' not in new_sub[2]


def test_change_subtitle_delay():
	sub = PATH+'/tests/subs/Matrix.eng.srt'
	millis = 5000
	new_sub = subtitles.change_subtitle_delay(millis, sub)
	
	assert new_sub[1] == '00:00:47,625 --> 00:00:49,751'

	millis = -4000
	new_sub = subtitles.change_subtitle_delay(millis, sub)
	
	assert new_sub[1] == '00:00:38,625 --> 00:00:40,751'
 
	with pytest.raises(SystemExit):
		subtitles.change_subtitle_delay(millis, 'sub')
	
	with pytest.raises(ValueError):
		subtitles.change_subtitle_delay(millis, -1)


def test_set_position():
	x = 100
	y = 50
	position = subtitles.set_position(axis_x=x, axis_y=y, one_subtitle=False)
	
	assert '{\\pos(100,50)}' == position

	position = subtitles.set_position(axis_x=x, one_subtitle=True)

	assert '{\\pos(100,268)}' == position

	position = subtitles.set_position(axis_y=y, one_subtitle=True)

	assert '{\\pos(192,50)}' == position


def test_format_millisecs_to_string():
	assert subtitles.format_millisecs_to_string(50000) == '00:00:50,000'
	assert subtitles.format_millisecs_to_string(500000) == '00:08:20,000'
	assert subtitles.format_millisecs_to_string(5000000) == '01:23:20,000'


def test_format_string_to_millisecs():
	assert subtitles.format_string_to_millisecs('00:00:42,625') == 42625
	assert subtitles.format_string_to_millisecs('00:00:44,751') == 44751
	assert subtitles.format_string_to_millisecs('00:00:56,014') == 56014
	assert subtitles.format_string_to_millisecs('00:00:58,641') == 58641
