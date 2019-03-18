# Initializing the data in mongo db container

This is a repository for a docker image to facilitate the process of initializing data in mongo db.

# Docker command
In docker command, it can be used as following:
```
docker -rm -d -v /you_local_data:/data --link mongo_db_container:mongo_db_container alancao/init_mongo_db:1.0.0 python app.py
```
## `your_local_data`
There should only contains two files in this folder, `db.cfg` and `[name].json`
### db.cfg
It includes the mongo db connection information.
```
[defaults]
db=mongo_db_container
db_port=37017
```
- `mongo_db_container` is the link name to the mongo db container

### [name].json
The value of `[name]` will be used as the `database name` in mongo server. The schema of this file would be as forllowing.
```
[
  {
    "collection": "collection_name",
    "items": [{"field1": "value1"}]
  }
]
```

# Plan
Currently, it doesn't support authentication. It will be added soon.

Any problem please connect me in email <zongying_cao@163.com> or post an [issue](https://github.com/cao5zy/py_mongo_initialization/issues).
