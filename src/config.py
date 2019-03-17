from assertpy import assert_that
import os

class cfg:
    def __init__(self, config_file = "./app.cfg"):
        assert_that(config_file).exists()
        
        def load_config(cfg_file_name):
            from os import path
            if not path.exists(cfg_file_name):
                raise ValueError("The {} configuration file is not existing at {}".format(os.path.abspath(cfg_file_name)))

            
            from configparser import ConfigParser

            config = ConfigParser()
            config.read(cfg_file_name)

            return config

        def load_sections(config, default_section_name = "defaults"):
            
            def load_defaults():
                if default_section_name not in config.sections():
                    raise ValueError("The {} is not set in app.cfg".format(default_section_name))
                                     
                self.defaults = dict(config[default_section_name])

            def load_other_sections():
                [(lambda seciton_name: setattr(self, section_name, dict(config(section_name))))(section_name) for section_name in config.sections() if section_name != default_section_name]


            load_defaults()
            load_other_sections()
            
        load_sections(load_config(config_file))


