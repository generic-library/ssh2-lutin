#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "ssh2 library"

def get_licence():
	return "BSD-3"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "libssh2"

def get_maintainer():
	return ["Sara Golemon <sarag@libssh2.org>"]

def get_version():
	return [1,7,0]

def configure(target, my_module):
	my_module.add_src_file([
	    'ssh2/src/crypt.c',
	    'ssh2/src/keepalive.c',
	    'ssh2/src/userauth.c',
	    'ssh2/src/scp.c',
	    'ssh2/src/os400qc3.c',
	    'ssh2/src/agent.c',
	    'ssh2/src/knownhost.c',
	    'ssh2/src/comp.c',
	    'ssh2/src/transport.c',
	    'ssh2/src/openssl.c',
	    'ssh2/src/kex.c',
	    'ssh2/src/pem.c',
	    'ssh2/src/channel.c',
	    'ssh2/src/libgcrypt.c',
	    'ssh2/src/mac.c',
	    'ssh2/src/publickey.c',
	    'ssh2/src/packet.c',
	    'ssh2/src/session.c',
	    'ssh2/src/misc.c',
	    'ssh2/src/version.c',
	    'ssh2/src/hostkey.c',
	    'ssh2/src/wincng.c',
	    'ssh2/src/sftp.c',
	    'ssh2/src/global.c',
	    ])
	my_module.add_flag('c', [
	    '-DLIBSSH2_DH_GEX_NEW=1',
	    '-DLIBSSH2_OPENSSL',
	    ])
	my_module.compile_version("c", 1989)
	my_module.add_depend('z')
	my_module.add_depend('openssl')
	my_module.add_path("ssh2/src")
	my_module.add_path("generate")
	my_module.add_header_file([
	    'ssh2/include/libssh2.h',
	    'ssh2/include/libssh2_publickey.h',
	    'ssh2/include/libssh2_sftp.h',
	    'generate/libssh2_config.h',
	    ],
	    destination_path="")
	return True
