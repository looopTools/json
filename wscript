#! /usr/bin/env python
# encoding: utf-8
from waflib.Tools.compiler_cxx import cxx_compiler

import sys

APPNAME = 'nlohmann-json'
VERSION = '1.0.0'

def options(opt):
    opt.load('compiler_cxx')

def configure(cnf) :
    # TODO FIGURE OUT HOW THIS WORKS, cause it is bloody awesome
    #cnf.check(lib=['cryptopp', 'pqxx', 'pq'])

    cnf.load('compiler_cxx')
    
    cnf.env.append_value('CXXFLAGS', ['-g', '-std=c++17', '-Wall', '-Werror', '-Wextra', '-O3'])        
    cnf.env.append_value('LINKFLAGS', ['-pthread'])


def build(bld):

    bld(name = 'nlohmann_json_includes',
        includes = './include',
        export_includes = './include'
    )

    bld.recurse('waf_example')
