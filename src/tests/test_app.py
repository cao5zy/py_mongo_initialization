from app import get_collection_name, get_data_file
from assertpy import assert_that
from codegenhelper import init_test_folder, remove_test_folder, test_root
from nose import with_setup
from helper import load_resource, resources_folder
import os

init_test_folder()

def load_for_get_data_file():
    load_resource('get_data_file')

@with_setup(load_for_get_data_file, remove_test_folder)
def test_get_data_file():
    assert_that(get_data_file(os.path.join(test_root(), 'get_data_file'))).is_equal_to(os.path.join(test_root(), 'get_data_file', 'data.json'))
    
def test_get_collection_name():
    assert_that(get_collection_name('/data/hello.json')).is_equal_to('hello')    
