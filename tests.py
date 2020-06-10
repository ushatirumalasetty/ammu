from unittest.mock import *
import uuid
import time
        
@patch.object(uuid, 'uuid4', return_value = 5)
def test_person_details(id_value):
    from practise import Usha
    my_class_obj = Usha(name="usha",age= "22")
    assert my_class_obj.id  is 5
    
@patch.object(time, 'time', return_value = '3')
def test_get_epoch_time_stamp_as_str(time_value):
    from practise import get_epoch_time_stamp_as_str
    get_epoch_time_stamp_as_str_obj = get_epoch_time_stamp_as_str()
    assert get_epoch_time_stamp_as_str_obj  is '3'

