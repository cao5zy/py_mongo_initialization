from fn import F
from assertpy import assert_that
import os
import re

def get_data_file(folderpath = "/data/"):
    assert_that(folderpath).exists()

    def dumy(filelist):
        assert_that(filelist).is_length(1)

        return os.path.join(folderpath, filelist[0])
   
    return dumy(list(filter(lambda n:re.match(r'^.*\.json$', n) != None,  os.listdir(folderpath))))
    

def get_collection_name(data_file):
    assert_that(data_file).matches(r'^(/[^/ ]*)+/?$')
    try:
        (_, filename) = os.path.split(data_file)
        (name, ext) = os.path.splitext(filename)
        return name
    except Exception as ex:
        print('get collection name error')
        print(ex)
        raise ex

def get_data(filepath):
    assert_that(filepath).exists()

    res =  demjson.decod_file(filepath)

    assert_that(res).is_instance_of(list).is_not_empty()

    return res

def write_data(db, collection_name,  data_arr):
    list([db[collection_name].insert_one(data) for data in data_arr])
    
def main():
    (F(get_data)>> \
     F(write_data, Db, get_collection_name(get_data_file())))(get_data_file())

if __name__ == '__main__':
    main()
