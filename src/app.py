import os
import re
import demjson
from fn import F
from assertpy import assert_that
from pymongo import MongoClient
from config import cfg

def get_data_file(folderpath="/data/"):
    assert_that(folderpath).exists()

    def dumy(filelist):
        assert_that(filelist).is_length(1)

        return os.path.join(folderpath, filelist[0])

    return dumy(list(filter( \
                             lambda n: re.match(r'^.*\.json$', n) is not None, \
                             os.listdir(folderpath) \
    )))

def get_db_name(data_file):
    assert_that(data_file).matches(r'^(/[^/ ]*)+/?$')
    try:
        (_, filename) = os.path.split(data_file)
        (name, _) = os.path.splitext(filename)
        return name
    except Exception as ex:
        print('get collection name error')
        print(ex)
        raise ex

def get_data(filepath):
    assert_that(filepath).exists()

    res = demjson.decode_file(filepath)

    assert_that(res).is_instance_of(list).is_not_empty()
    assert_that(res[0]).contains_key('collection', 'items', 'keys')

    return res

def write_data(db_client, db_name, data_arr):
    def insert(collection_name, arr, keys):
        assert_that(collection_name).is_not_empty()
        assert_that(keys).is_not_empty()
        assert_that(arr).is_not_empty()

        def not_existing(data):
            def get_args():
                def dumy(dict_data):
                    def setval(key):
                        dict_data[key] = data[key]

                    list([setval(key) for key in keys])
                    assert_that(dict).is_not_empty()
                    
                    return dict

                return dumy({})
                
            def get_existing():
                return db_client[db_name][collection_name].find(get_args())
                
            return True if keys is None else get_existing() is None
        
        def insert_item(data):
            assert_that(data).is_type_of(dict)

            db_client[db_name][collection_name].insert_one(data)

        list([insert_item(data) for data in arr if not_existing(data)])
        
    list([insert(data['collection'], data['items'], data['keys']) for data in data_arr])

def get_connection_info(config_file='/data/db.cfg'):
    assert_that(config_file).exists()

    defaults = cfg(config_file).defaults

    return defaults
    
def get_db_client(connection_info):
    assert_that(connection_info).contains_key('db', 'db_port')
    return MongoClient("mongodb://{}:{}".format(connection_info['db'], connection_info['db_port']))


def main():
    (F(get_data)>> \
     F(write_data, \
       get_db_client(get_connection_info()), \
       get_db_name(get_data_file())\
     )
    )(get_data_file())

if __name__ == '__main__':
    main()
