from fn import F
from assertpy import assert_that
import os
import re
import demjson

def get_data_file(folderpath = "/data/"):
    assert_that(folderpath).exists()

    def dumy(filelist):
        assert_that(filelist).is_length(1)

        return os.path.join(folderpath, filelist[0])
   
    return dumy(list(filter(lambda n:re.match(r'^.*\.json$', n) != None,  os.listdir(folderpath))))
    

def get_db_name(data_file):
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

    res =  demjson.decode_file(filepath)

    assert_that(res).is_instance_of(list).is_not_empty()
    assert_that(res[0]).contains_key('collection', 'items')

    return res

def write_data(conn, db_name,  data_arr):
    list([conn[db_name][data['collection']].insert_one(data['items']) for data in data_arr])

def get_db():
    pass

def main():
    (F(get_data)>> \
     F(write_data, get_db(), get_db_name(get_data_file())))(get_data_file())

if __name__ == '__main__':
    main()
