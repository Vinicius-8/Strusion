import pytest

#importing from parent folder
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


PATH = sys.path[0]

import IO

def test_load_subtitle():
	sub = PATH+'/tests/subs/Matrix.eng.srt'
	sub2 = PATH+'/tests/subs/Matrix.por.srt'
	
	assert type(IO.load(sub)) == list
	assert type(IO.load(sub2)) == list


def test_output_file():
	file = PATH+'/tests/temp_sub.srt'
	IO.output_file(file, [1, 2, 3])
	try:
		assert os.path.exists(file) == True
	finally:
		os.remove(file)



