import pytest

#importing from parent folder
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


PATH = sys.path[0]

import strusion


def test_config_default_output():
	
	sub = strusion.config_default_output('my_subtitle.srt')

	assert sub == 'my_subtitle.mod.srt'

	#with pytest.raises(Exception):
	#	strusion.config_default_output('my_subtitle.ass')



def test_is_srt():
	sub = strusion.is_srt('my_subtitle.srt')

	assert sub == True

	sub = strusion.is_srt('my_subtitle.srv')

	assert sub == False