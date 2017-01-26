#!/usr/env/bin python
# -*- coding: utf-8 -*-
#
# CAVEAT UTILITOR
# This file was automatically generated by Grako.
#    https://bitbucket.org/apalala/grako/
# Any changes you make to it will be overwritten the
# next time the file is generated.
#

from __future__ import print_function, division, absolute_import, unicode_literals
from grako.parsing import * # @UnusedWildImport
from grako.exceptions import * # @UnusedWildImport

__version__ = '17.026.14.12.33'

class urlGramParser(Parser):
    @rule_def
    def sipURL(self):
        self.schema()
        self.colon()
        with self._optional():
            self.userinfo()
        self.hostport()

    @rule_def
    def schema(self):
        with self._choice():
            with self._option():
                self._token('sip')
            with self._option():
                self._token('sips')
            self._error('expecting one of: sips sip')

    @rule_def
    def colon(self):
        self._token(':')

    @rule_def
    def userinfo(self):
        self.user()
        with self._optional():
            self.colon()
            self.password()
        self.atmark()

    @rule_def
    def atmark(self):
        self._token('@')

    @rule_def
    def password(self):
        self._pattern(r'[a-z]*')

    @rule_def
    def user(self):
        self._pattern(r'[a-z]*')

    @rule_def
    def hostport(self):
        self.host()
        with self._optional():
            self.colon()
            self.port()

    @rule_def
    def host(self):
        self._pattern(r'[a-z]*[.][a-z]*')

    @rule_def
    def port(self):
        self._pattern(r'[1-9][0-9]*')



class urlGramSemanticParser(CheckSemanticsMixin, urlGramParser):
    pass


class urlGramSemantics(object):
    def sipURL(self, ast):
        return ast

    def schema(self, ast):
        return ast

    def colon(self, ast):
        return ast

    def userinfo(self, ast):
        return ast

    def atmark(self, ast):
        return ast

    def password(self, ast):
        return ast

    def user(self, ast):
        return ast

    def hostport(self, ast):
        return ast

    def host(self, ast):
        return ast

    def port(self, ast):
        return ast

def main(filename, startrule):
    import json
    with open(filename) as f:
        text = f.read()
    parser = urlGramParser(parseinfo=False)
    ast = parser.parse(text, startrule, filename=filename)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import sys
    if '-l' in sys.argv:
        print('Rules:')
        for r in urlGramParser.rule_list():
            print(r)
        print()
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print('Usage:')
        program = sys.argv[0].split('/')[-1]
        print(program, ' <filename> <startrule>')
        print(program, ' -l') # list rules
        print(program, ' -h')