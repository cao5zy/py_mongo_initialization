from codegenhelper import init_test_folder, remove_test_folder, test_root, put_folder
import shutil
import os
from assertpy import assert_that

resources_folder = './test_resources/'

def load_resource(resource_name, folderpath = resources_folder):
    def copy(source_folder, target_folder):
        assert_that(source_folder).exists()
        shutil.copytree(source_folder, os.path.join(target_folder, resource_name))
        assert_that(os.path.join(target_folder, resource_name)).exists()
        
    copy(os.path.join(folderpath, resource_name), test_root())
    
