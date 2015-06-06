#!/usr/bin/env python
import logging
import os
import sys


base_package_folder_name = "base_packages"
libtool_relative_path = base_package_folder_name +"/libtool"
external_app_folder_name = "external_app_repos"
base_setting_folder_name = "django18_server"


my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(my_path, libtool_relative_path))
from libtool import include_all, get_folder
include_all(__file__, base_package_folder_name)
include_all(__file__, external_app_folder_name)


def initialize_settings():
    from djangoautoconf import DjangoAutoConf
    c = DjangoAutoConf()
    c.set_base_extra_settings_list([])
    c.set_external_app_repositories("external_app_repos")
    c.set_default_settings(base_setting_folder_name + ".settings")
    c.set_root_dir(get_folder(__file__))
    c.add_extra_settings_from_folder()
    c.configure()


if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django18_server.settings")
    # logging.basicConfig(level=logging.DEBUG)
    initialize_settings()
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
