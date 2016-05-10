#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "BINARY"

def get_sub_type():
	return "TEST"

def get_desc():
	return "ssh2 sample"

def get_licence():
	return "BSD-3"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "libssh2"

def get_maintainer():
	return ["Sara Golemon <sarag@libssh2.org>"]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'ssh2/tests/ssh2.c',
	    ])
	my_module.compile_version("c", 1989)
	my_module.add_module_depend('ssh2')
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "ssh2", "tests"))
	return my_module


