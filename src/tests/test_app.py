from app import get_db_name, get_data_file, get_data
from assertpy import assert_that
from codegenhelper import init_test_folder, remove_test_folder, test_root
from nose import with_setup
from helper import load_resource, resources_folder
import os

init_test_folder()

def load_for_get_data_file():
    load_resource('get_data_file')

def load_for_get_data_file_error_case():
    load_resource('get_data_file_error_case')
    
@with_setup(load_for_get_data_file, remove_test_folder)
def test_get_data_file():
    assert_that(get_data_file(os.path.join(test_root(), 'get_data_file'))).is_equal_to(os.path.join(test_root(), 'get_data_file', 'data.json'))

@with_setup(load_for_get_data_file_error_case, remove_test_folder)
def test_get_data_file_will_cause_error():
    assert_that(get_data_file).raises(AssertionError).when_called_with(os.path.join(test_root(), 'get_data_file_error_case'))

def test_get_db_name():
    assert_that(get_db_name('/data/hello.json')).is_equal_to('hello')    

def load_for_get_data():
    load_resource('get_data_file')

@with_setup(load_for_get_data, remove_test_folder)
def test_get_data():
    assert_that(get_data(get_data_file(os.path.join(test_root(), 'get_data_file')))).is_not_empty()
