from config import cfg
from assertpy import assert_that
from codegenhelper import init_test_folder, remove_test_folder, test_root
from nose import with_setup
from helper import load_resource
import os

init_test_folder()

def load_for_config():
    load_resource('get_data_file')

@with_setup(load_for_config, remove_test_folder)    
def test_config():

    def dumy(config):
        assert_that(config.defaults).contains_entry({'db': 'service1'}).contains_entry({'db_port':'232'})

    dumy(cfg(os.path.join(test_root(), 'get_data_file', 'db.cfg')))
